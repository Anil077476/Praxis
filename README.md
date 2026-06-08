# Praxis - Practice and Action 🚀

> A repository demonstrating GitHub mechanics and contribution tracking through automated activity generation.

## 📋 About

**Praxis** is an educational project that showcases how GitHub contribution graphs work. It contains an automated script that generates commit history to populate the GitHub activity graph for demonstration purposes.

> ⚠️ **Disclaimer**: This project is for educational purposes only. It demonstrates GitHub mechanics and should not be used to misrepresent professional contributions or actual coding activity.

## 🎯 What This Project Does

The `contribute.py` script automatically generates:
- **Realistic commit history** across a specified time period
- **Variable commit frequency** (customizable per day)
- **Natural distribution** of activity (weekdays, weekends, etc.)
- **Automatic GitHub push** to visualize activity on your profile

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Git installed and configured
- GitHub account with SSH/HTTPS access configured

### Installation & Usage

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Anil077476/Praxis.git
   cd Praxis
   ```

2. **Run the activity generator:**
   ```bash
   python contribute.py
   ```

3. **Wait for GitHub to update** (5-10 minutes)

4. **Check your profile:**
   - Visit https://github.com/Anil077476
   - Your contribution graph will be updated

## 🎨 Customization Options

### Default Behavior
```bash
python contribute.py
```
- Commits on ~70% of days in the last year
- 1-12 commits per day
- Includes weekends
- Automatically pushes to your repo

### Custom Settings

**Example 1: More aggressive activity**
```bash
python contribute.py --max_commits=20 --frequency=80
```
- 20 commits per day maximum
- 80% of days will have commits

**Example 2: Weekdays only**
```bash
python contribute.py --no_weekends
```
- Skips Saturday and Sunday

**Example 3: Specific date range**
```bash
python contribute.py --days_before=180 --days_after=30
```
- Generates commits for 180 days in the past and 30 days in the future

## 📊 How It Works

1. **Initialize**: Creates a local git repository
2. **Generate**: Creates commits with dated timestamps across specified period
3. **Add History**: Each commit adds an entry to `contributions.txt`
4. **Push**: Uploads all commits to your GitHub repository
5. **Display**: GitHub reindexes and updates your contribution graph

## 🔧 Script Options

| Option | Default | Description |
|--------|---------|-------------|
| `--max_commits` | 12 | Maximum commits per day |
| `--frequency` | 70 | Percentage of days with commits (0-100) |
| `--days_before` | 365 | Days before today to start |
| `--days_after` | 0 | Days after today to continue |
| `--no_weekends` | False | Skip Saturday & Sunday |

## ❓ Troubleshooting

### Activity not showing up?
1. **Wait longer** - GitHub takes 5-10 minutes to reindex
2. **Refresh browser** - Clear cache and reload your profile
3. **Check email** - Ensure your git email matches your GitHub email:
   ```bash
   git config --get user.email
   ```

### Email mismatch?
Update your git configuration:
```bash
git config --global user.email "your-github-email@example.com"
```

### Still not working?
1. Verify commits were pushed: `git log`
2. Check your GitHub privacy settings (enable showing private contributions if applicable)
3. Create a fresh test repository and try again

## 📚 Educational Value

This project demonstrates:
- ✅ Git commit history manipulation
- ✅ GitHub API integration
- ✅ Contribution graph mechanics
- ✅ Batch automation with Python
- ✅ Time-based data generation

## 📝 Files

- `contribute.py` - Main activity generator script
- `contributions.txt` - Log file created during execution
- `README.md` - This file

## 🔐 Privacy & Security

- ✅ No sensitive data is stored or transmitted
- ✅ Script is open-source and auditable
- ✅ Uses standard Git and GitHub authentication
- ✅ No external API calls or tracking

## ⚖️ Legal & Ethical Notice

This tool is provided for **educational and demonstration purposes**. Users are responsible for:
- Not misrepresenting contribution history on professional profiles
- Not using this to deceive employers or collaborators
- Understanding GitHub's terms of service
- Using this ethically and responsibly

## 🌟 Related Projects

After learning Git mechanics, check out these real projects:
- [sol4k](https://github.com/sol4k/sol4k) - Kotlin/JVM Solana client
- [podil.js](https://github.com/podil/podil.js) - Database migration tool
- [goxygen](https://github.com/goxygen/goxygen) - Web project generator
- [zeit](https://github.com/zeit/zeit) - Fitbit clock face

## 📄 License

This project is provided as-is for educational purposes.

## 🤝 Contributing

This is an educational project. If you find improvements or issues:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📧 Contact

For questions or issues: [Open an issue](https://github.com/Anil077476/Praxis/issues)

---

**Made with ❤️ for learning and understanding GitHub mechanics**

*Last Updated: June 8, 2026*
