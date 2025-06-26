import subprocess
import os

def run_complete_automation():
    print("🤖 Starting Simple Image Testing Automation")
    print("=" * 45)
    
    # Step 1: Find images if CSV doesn't exist
    if not os.path.exists('images.csv'):
        print("📋 Step 1: Finding images...")
        subprocess.run(['python', 'find_images.py'])
    else:
        print("📋 Step 1: Using existing images.csv")
    
    # Step 2: Run tests
    print("\n🧪 Step 2: Running automated tests...")
    subprocess.run(['pytest', 'test_images.py', '-v'])
    
    print("\n✅ Automation complete!")

if __name__ == "__main__":
    run_complete_automation()