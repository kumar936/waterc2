"""
Automated Logo Replacement Script
This script updates dashboard_with_live_ml.html to use the new water-logo.png
"""

import shutil
import os

print("="*70)
print("  DASHBOARD LOGO FIX SCRIPT")
print("="*70)
print()

# Step 1: Copy the new logo file
print("Step 1: Copying new logo file...")
try:
    shutil.copy("1769404035774_water-supply.png", "water-logo.png")
    print("✓ Logo file copied: water-logo.png")
except Exception as e:
    print(f"✗ Error copying logo: {e}")
    print("  Please manually copy the file and rename to 'water-logo.png'")

print()

# Step 2: Read the dashboard HTML
print("Step 2: Reading dashboard file...")
try:
    with open('dashboard_with_live_ml.html', 'r', encoding='utf-8') as f:
        content = f.read()
    print("✓ Dashboard file loaded")
except Exception as e:
    print(f"✗ Error reading file: {e}")
    exit(1)

print()

# Step 3: Replace logo references
print("Step 3: Replacing logo references...")

# Count replacements
replacements_made = 0

# Replace 1: CSS background-image
old_css = 'background-image: url("WhatsApp Image 2026-01-24 at 5.47.57 PM.jpeg");'
new_css = '''background-image: url("water-logo.png");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;'''

if old_css in content:
    content = content.replace(old_css, new_css)
    replacements_made += 1
    print("✓ Replaced CSS background-image reference")

# Replace 2: IMG src (header logo)
old_img = 'src="WhatsApp Image 2026-01-24 at 5.47.57 PM.jpeg"'
new_img = 'src="water-logo.png"'

if old_img in content:
    content = content.replace(old_img, new_img)
    replacements_made += 1
    print("✓ Replaced IMG src reference")

# Replace 3: Improve img styling
old_style = 'style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;"'
new_style = 'style="width: 45px; height: 45px; object-fit: contain; background: white; padding: 8px; border-radius: 50%; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"'

if old_style in content:
    content = content.replace(old_style, new_style)
    replacements_made += 1
    print("✓ Updated logo styling")

# Replace 4: Alt text
if 'alt="Water Logo"' in content:
    content = content.replace('alt="Water Logo"', 'alt="Water Supply Logo"')
    print("✓ Updated alt text")

print()
print(f"Total replacements made: {replacements_made}")
print()

# Step 4: Backup original file
print("Step 4: Creating backup...")
try:
    shutil.copy('dashboard_with_live_ml.html', 'dashboard_with_live_ml_BACKUP.html')
    print("✓ Backup created: dashboard_with_live_ml_BACKUP.html")
except Exception as e:
    print(f"⚠ Could not create backup: {e}")

print()

# Step 5: Write updated content
print("Step 5: Saving updated dashboard...")
try:
    with open('dashboard_with_live_ml_FIXED.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Updated dashboard saved: dashboard_with_live_ml_FIXED.html")
    print()
    print("="*70)
    print("  SUCCESS!")
    print("="*70)
    print()
    print("Next steps:")
    print("1. Open 'dashboard_with_live_ml_FIXED.html' in your browser")
    print("2. Verify the logo appears correctly")
    print("3. If it looks good, replace the original:")
    print("   - Delete: dashboard_with_live_ml.html")
    print("   - Rename: dashboard_with_live_ml_FIXED.html → dashboard_with_live_ml.html")
    print()
    print("Your original file is backed up as:")
    print("   dashboard_with_live_ml_BACKUP.html")
    print()
except Exception as e:
    print(f"✗ Error saving file: {e}")
    exit(1)

print("="*70)
