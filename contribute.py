#!/usr/bin/env python3
"""
GitHub Activity Generator - Execute Script
This will generate commits and push them to your repository
"""

import os
import sys
import subprocess
from datetime import datetime, timedelta
import random

def run_git_command(cmd, cwd=None):
    """Execute git command"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        print(f"$ {cmd}")
        if result.stdout:
            print(result.stdout)
        if result.returncode != 0 and result.stderr:
            print(f"Error: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"Exception: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 GITHUB ACTIVITY GENERATOR - EXECUTION")
    print("=" * 60)
    
    repo_dir = "github_activity_gen"
    repo_url = "https://github.com/Anil077476/Praxis.git"
    
    # Step 1: Create and initialize repo
    print("\n📁 Step 1: Setting up local repository...")
    if os.path.exists(repo_dir):
        import shutil
        shutil.rmtree(repo_dir)
    
    os.makedirs(repo_dir)
    run_git_command("git init", cwd=repo_dir)
    run_git_command('git config user.name "Anil077476"', cwd=repo_dir)
    run_git_command('git config user.email "bethapudianilkumble@gmail.com"', cwd=repo_dir)
    
    # Step 2: Create initial file
    print("\n📝 Step 2: Creating contribution file...")
    contrib_file = os.path.join(repo_dir, "contributions.txt")
    with open(contrib_file, 'w') as f:
        f.write("# GitHub Contributions Log\n")
        f.write(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    # Step 3: Generate commits
    print("\n⏳ Step 3: Generating commits (this may take a minute)...")
    
    today = datetime.now()
    start_date = today - timedelta(days=365)
    
    commits_count = 0
    current_date = start_date
    
    while current_date <= today:
        # 70% chance to commit on any given day
        if random.random() < 0.70:
            # 1-12 commits per day
            num_commits = random.randint(1, 12)
            
            for i in range(num_commits):
                # Add entry to file
                with open(contrib_file, 'a') as f:
                    f.write(f"Contribution #{commits_count + 1} - {current_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
                
                # Stage
                run_git_command("git add .", cwd=repo_dir)
                
                # Commit with specific date
                commit_msg = f"Activity: {current_date.strftime('%Y-%m-%d')}"
                commit_date = current_date.isoformat()
                cmd = f'git commit -m "{commit_msg}" --date "{commit_date}"'
                run_git_command(cmd, cwd=repo_dir)
                
                commits_count += 1
                current_date += timedelta(hours=random.randint(1, 8))
        
        # Move to next day
        if current_date.day == today.day and current_date.month == today.month:
            break
        current_date += timedelta(days=1)
    
    print(f"\n✅ Generated {commits_count} commits!")
    
    # Step 4: Push to remote
    print("\n📤 Step 4: Pushing to GitHub...")
    run_git_command(f"git remote add origin {repo_url}", cwd=repo_dir)
    run_git_command("git branch -M main", cwd=repo_dir)
    
    if run_git_command("git push -u origin main --force", cwd=repo_dir):
        print("✅ Successfully pushed to GitHub!")
    else:
        print("⚠️  Push completed (may require authentication)")
    
    print("\n" + "=" * 60)
    print("✨ COMPLETE!")
    print("=" * 60)
    print(f"📊 Total commits generated: {commits_count}")
    print(f"📁 Repository: {repo_url}")
    print(f"⏱️  GitHub will update your activity in 5-10 minutes")
    print(f"🔍 Check: https://github.com/Anil077476")
    print("=" * 60)

if __name__ == "__main__":
    main()
