#!/usr/bin/env python3
"""
GitHub Activity Generator
Generates commit history to populate GitHub contribution graph
"""

import os
import sys
import argparse
import random
from datetime import datetime, timedelta
import subprocess

def run_command(command, cwd=None):
    """Execute a shell command"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Error executing command: {e}")
        return False

def initialize_repo(repo_path):
    """Initialize a new git repository"""
    os.makedirs(repo_path, exist_ok=True)
    run_command("git init", cwd=repo_path)
    run_command("git config user.email 'contributor@example.com'", cwd=repo_path)
    run_command("git config user.name 'Contributor'", cwd=repo_path)

def create_contribution_file(repo_path):
    """Create a file to hold contributions"""
    file_path = os.path.join(repo_path, "contributions.txt")
    with open(file_path, 'w') as f:
        f.write("GitHub Contributions\n")
    return file_path

def generate_commits(repo_path, contribution_file, days_before, days_after, 
                    max_commits, frequency, no_weekends):
    """Generate commits for the specified date range"""
    
    today = datetime.now()
    start_date = today - timedelta(days=days_before)
    end_date = today + timedelta(days=days_after)
    
    current_date = start_date
    commits_generated = 0
    
    while current_date <= end_date:
        # Skip weekends if requested
        if no_weekends and current_date.weekday() >= 5:
            current_date += timedelta(days=1)
            continue
        
        # Randomly decide whether to commit on this day based on frequency
        if random.random() * 100 < frequency:
            # Randomly decide number of commits for this day
            num_commits = random.randint(1, max_commits)
            
            for i in range(num_commits):
                # Append to contribution file
                with open(contribution_file, 'a') as f:
                    f.write(f"Contribution on {current_date.date()} at {current_date.time()}\n")
                
                # Stage and commit
                run_command("git add .", cwd=repo_path)
                
                # Create commit with the specified date
                commit_date = current_date.isoformat()
                commit_command = f'git commit --allow-empty -m "Contribution on {current_date.date()}" --date "{commit_date}"'
                
                if run_command(commit_command, cwd=repo_path):
                    commits_generated += 1
                
                current_date += timedelta(hours=random.randint(1, 8))
        
        current_date += timedelta(days=1)
    
    return commits_generated

def push_to_remote(repo_path, remote_url):
    """Push commits to remote repository"""
    run_command("git remote add origin " + remote_url, cwd=repo_path)
    run_command("git branch -M main", cwd=repo_path)
    return run_command("git push -u origin main", cwd=repo_path)

def main():
    parser = argparse.ArgumentParser(
        description='Generate GitHub contributions for the last year'
    )
    parser.add_argument('--repository', type=str, help='Remote repository URL (SSH or HTTPS)')
    parser.add_argument('--max_commits', type=int, default=20, 
                       help='Maximum commits per day (default: 20)')
    parser.add_argument('--frequency', type=int, default=50,
                       help='Frequency of commits as percentage (default: 50)')
    parser.add_argument('--days_before', type=int, default=365,
                       help='Days before today to start commits (default: 365)')
    parser.add_argument('--days_after', type=int, default=0,
                       help='Days after today to end commits (default: 0)')
    parser.add_argument('--no_weekends', action='store_true',
                       help='Skip weekends')
    
    args = parser.parse_args()
    
    print("🚀 GitHub Activity Generator")
    print("=" * 50)
    
    # Create temporary directory for repo
    repo_path = "github_contributions"
    
    # Clean up if exists
    if os.path.exists(repo_path):
        import shutil
        shutil.rmtree(repo_path)
    
    print(f"📁 Initializing repository at {repo_path}...")
    initialize_repo(repo_path)
    
    print("📝 Creating contribution file...")
    contrib_file = create_contribution_file(repo_path)
    
    print("⏳ Generating commits...")
    print(f"   Max commits per day: {args.max_commits}")
    print(f"   Frequency: {args.frequency}%")
    print(f"   Days before: {args.days_before}")
    print(f"   Days after: {args.days_after}")
    print(f"   Skip weekends: {args.no_weekends}")
    
    commits = generate_commits(
        repo_path, 
        contrib_file,
        args.days_before,
        args.days_after,
        args.max_commits,
        args.frequency,
        args.no_weekends
    )
    
    print(f"✅ Generated {commits} commits!")
    
    if args.repository:
        print(f"📤 Pushing to {args.repository}...")
        if push_to_remote(repo_path, args.repository):
            print("✅ Successfully pushed to remote!")
        else:
            print("❌ Failed to push to remote")
    else:
        print(f"⚠️  No repository URL provided. Repository is ready at: {repo_path}")
        print("   You can push it manually later.")
    
    print("=" * 50)
    print("✨ Done! GitHub may take a few minutes to update your activity graph.")

if __name__ == "__main__":
    main()
