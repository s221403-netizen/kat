def create_profile_html():
    """Generate an HTML profile page with personal information"""
    
    # Profile information
    profile = {
        'name': 'John Doe',
        'age': '25',
        'school': 'University of Technology',
        'major': 'Computer Science',
        'year': 'Senior',
        'hometown': 'San Francisco, CA',
        'email': 'john.doe@example.com',
        'github': 'github.com/johndoe',
        'linkedin': 'linkedin.com/in/johndoe',
        'bio': 'Passionate computer science student with interests in web development and artificial intelligence. Love building creative solutions to real-world problems.',
        'skills': ['Python', 'JavaScript', 'HTML/CSS', 'Java', 'SQL', 'React']
    }
    
    # HTML template
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{profile['name']} - Profile</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            
            .profile-card {{
                max-width: 800px;
                width: 100%;
                background: white;
                border-radius: 20px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.1);
                overflow: hidden;
                animation: fadeIn 1s ease-in;
            }}
            
            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            
            .profile-header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px;
                text-align: center;
            }}
            
            .profile-header h1 {{
                font-size: 2.5em;
                margin-bottom: 10px;
            }}
            
            .profile-header .title {{
                font-size: 1.2em;
                opacity: 0.95;
            }}
            
            .profile-body {{
                padding: 40px;
            }}
            
            .info-section {{
                margin-bottom: 30px;
            }}
            
            .info-section h2 {{
                color: #764ba2;
                border-bottom: 2px solid #667eea;
                padding-bottom: 10px;
                margin-bottom: 20px;
                font-size: 1.5em;
            }}
            
            .info-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
            }}
            
            .info-item {{
                padding: 15px;
                background: #f8f9fa;
                border-radius: 10px;
                transition: transform 0.3s ease;
            }}
            
            .info-item:hover {{
                transform: translateY(-5px);
                box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2);
            }}
            
            .info-label {{
                font-weight: bold;
                color: #667eea;
                display: block;
                margin-bottom: 5px;
            }}
            
            .info-value {{
                color: #333;
            }}
            
            .bio {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 25px;
                border-radius: 10px;
                margin-bottom: 30px;
            }}
            
            .bio h3 {{
                margin-bottom: 10px;
                font-size: 1.3em;
            }}
            
            .bio p {{
                line-height: 1.6;
                opacity: 0.95;
            }}
            
            .skills {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 15px;
            }}
            
            .skill-tag {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 0.9em;
                font-weight: 500;
                transition: transform 0.3s ease;
            }}
            
            .skill-tag:hover {{
                transform: scale(1.05);
            }}
            
            .contact-links {{
                display: flex;
                gap: 15px;
                justify-content: center;
                margin-top: 20px;
            }}
            
            .contact-link {{
                color: white;
                text-decoration: none;
                padding: 10px 20px;
                border-radius: 25px;
                background: rgba(255,255,255,0.2);
                transition: background 0.3s ease;
            }}
            
            .contact-link:hover {{
                background: rgba(255,255,255,0.3);
            }}
            
            @media (max-width: 600px) {{
                .profile-header {{
                    padding: 30px;
                }}
                
                .profile-header h1 {{
                    font-size: 2em;
                }}
                
                .profile-body {{
                    padding: 25px;
                }}
                
                .info-grid {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="profile-card">
            <div class="profile-header">
                <h1>{profile['name']}</h1>
                <div class="title">{profile['major']} Student</div>
                <div class="contact-links">
                    <a href="mailto:{profile['email']}" class="contact-link">Email</a>
                    <a href="https://{profile['github']}" class="contact-link" target="_blank">GitHub</a>
                    <a href="https://{profile['linkedin']}" class="contact-link" target="_blank">LinkedIn</a>
                </div>
            </div>
            
            <div class="profile-body">
                <div class="bio">
                    <h3>About Me</h3>
                    <p>{profile['bio']}</p>
                </div>
                
                <div class="info-section">
                    <h2>Personal Information</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <span class="info-label">Age</span>
                            <span class="info-value">{profile['age']} years</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">School</span>
                            <span class="info-value">{profile['school']}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Major</span>
                            <span class="info-value">{profile['major']}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Year</span>
                            <span class="info-value">{profile['year']}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Hometown</span>
                            <span class="info-value">{profile['hometown']}</span>
                        </div>
                    </div>
                </div>
                
                <div class="info-section">
                    <h2>Skills</h2>
                    <div class="skills">
    """
    
    # Add skills dynamically
    for skill in profile['skills']:
        html_content += f'                        <span class="skill-tag">{skill}</span>\n'
    
    html_content += """
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Save to file
    filename = "profile.html"
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"✅ Profile HTML file created successfully: {filename}")
        print(f"📍 File location: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error creating file: {e}")
        return False

def main():
    """Main function to create the profile HTML"""
    print("🚀 Creating profile HTML file...")
    print("-" * 40)
    
    # Create the profile HTML
    if create_profile_html():
        print("\n✨ You can customize the profile by editing the 'profile' dictionary in the code!")
        print("🌐 Open profile.html in your web browser to view your profile.")
    else:
        print("\n❌ Failed to create profile HTML file.")

if __name__ == "__main__":
    main()