import os
from datetime import datetime
import re


class OutputFormatter:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_html(self, content, origin, cities, date_range, interests):
        """Generate beautiful HTML format travel plan"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"trip_plan_{timestamp}.html"
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Plan - {cities}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.8em;
            margin-bottom: 10px;
            font-weight: 300;
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .trip-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .info-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            border-left: 4px solid #4facfe;
        }}
        
        .info-card h3 {{
            color: #4facfe;
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .content h2 {{
            color: #4facfe;
            border-bottom: 2px solid #4facfe;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }}
        
        .travel-content {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            border-left: 5px solid #4facfe;
            white-space: pre-line;
            font-size: 1.1em;
            line-height: 1.8;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                margin: 10px;
                border-radius: 10px;
            }}
            
            .header {{
                padding: 20px 15px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            .trip-info, .content {{
                padding: 20px 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Your Personalized Travel Plan 🌟</h1>
            <p>Carefully crafted by AI Travel Expert Team</p>
        </div>
        
        <div class="trip-info">
            <div class="info-card">
                <h3>📍 Departure Location</h3>
                <p>{origin}</p>
            </div>
            <div class="info-card">
                <h3>🏙️ Destination Cities</h3>
                <p>{cities}</p>
            </div>
            <div class="info-card">
                <h3>📅 Travel Dates</h3>
                <p>{date_range}</p>
            </div>
            <div class="info-card">
                <h3>🎯 Interests & Preferences</h3>
                <p>{interests}</p>
            </div>
        </div>
        
        <div class="content">
            <h2>📋 Complete Itinerary</h2>
            <div class="travel-content">{content}</div>
        </div>
        
        <div class="footer">
            <p>📱 Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | 🤖 Created by CrewAI Travel Expert Team</p>
        </div>
    </div>
</body>
</html>
        """
        
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath
    
    def generate_markdown(self, content, origin, cities, date_range, interests):
        """Generate Markdown format travel plan"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"trip_plan_{timestamp}.md"
        
        # Clean content, remove extra formatting
        clean_content = re.sub(r'\*\*|\*', '', content)
        
        markdown_content = f"""# 🌟 Travel Plan - {cities}

> Carefully crafted by CrewAI Travel Expert Team  
> Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## 📋 Travel Information

| Item | Details |
|------|------|
| 📍 **Departure Location** | {origin} |
| 🏙️ **Destination Cities** | {cities} |
| 📅 **Travel Dates** | {date_range} |
| 🎯 **Interests & Preferences** | {interests} |

---

## 🗺️ Complete Itinerary

{clean_content}

---

## 📱 Generation Information

- **Creation Tool**: CrewAI Travel Expert Team
- **AI Model**: GPT-4o-mini
- **Search Tool**: SerperDev API
- **Generated Time**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

> 💡 **Note**: This itinerary is generated based on currently available information. Please verify the latest prices, opening hours, and booking information before your actual trip.

"""
        
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        return filepath
    
    def generate_text(self, content, origin, cities, date_range, interests):
        """Generate plain text format travel plan"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"trip_plan_{timestamp}.txt"
        
        text_content = f"""
{'='*80}
                    🌟 Travel Plan - {cities} 🌟
{'='*80}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Carefully crafted by CrewAI Travel Expert Team

{'='*80}
Travel Information
{'='*80}

📍 Departure Location: {origin}
🏙️ Destination Cities: {cities}
📅 Travel Dates: {date_range}
🎯 Interests & Preferences: {interests}

{'='*80}
Complete Itinerary
{'='*80}

{content}

{'='*80}
Generation Information
{'='*80}

Creation Tool: CrewAI Travel Expert Team
AI Model: GPT-4o-mini
Search Tool: SerperDev API
Generated Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

💡 Note: This itinerary is generated based on currently available information.
Please verify the latest prices, opening hours, and booking information before your actual trip.

{'='*80}
        """
        
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        return filepath
    
    def save_all_formats(self, content, origin, cities, date_range, interests):
        """Save all format files"""
        files_created = {}
        
        try:
            files_created['html'] = self.generate_html(content, origin, cities, date_range, interests)
            files_created['markdown'] = self.generate_markdown(content, origin, cities, date_range, interests)
            files_created['text'] = self.generate_text(content, origin, cities, date_range, interests)
        except Exception as e:
            print(f"Error occurred while generating files: {e}")
        
        return files_created