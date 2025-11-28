# S13/04402/21 - SETH OMONDI OTIENO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import warnings
warnings.filterwarnings('ignore')

# Load crime data
try:
    crime_df = pd.read_csv('crime_data.csv')
    print(f"Loaded {crime_df.shape[0]:,} crime records")
except FileNotFoundError:
    try:
        crime_df = pd.read_csv('los_angeles_crime.csv')
        print(f"Loaded {crime_df.shape[0]:,} crime records")
    except FileNotFoundError:
        try:
            crime_df = pd.read_csv('crime.csv')
            print(f"Loaded {crime_df.shape[0]:,} crime records")
        except FileNotFoundError:
            print("Crime dataset not found")
            print("Download from DataCamp 'Analyzing Crime in Los Angeles'")
            raise

print("\nDataset preview:")
print(crime_df.head(3))
print(f"\nColumns: {crime_df.columns.tolist()}")

# Standardize column names
crime_df.columns = crime_df.columns.str.lower().str.replace(' ', '_')
print(f"\nStandardized columns: {crime_df.columns.tolist()}")

# Identify key columns
date_cols = [col for col in crime_df.columns if any(word in col for word in ['date', 'time'])]
crime_type_cols = [col for col in crime_df.columns if any(word in col for word in ['crime', 'offense', 'type'])]
area_cols = [col for col in crime_df.columns if any(word in col for word in ['area', 'district', 'precinct'])]
location_cols = [col for col in crime_df.columns if any(word in col for word in ['lat', 'lon', 'location'])]

main_date = date_cols[0] if date_cols else None
main_crime_type = crime_type_cols[0] if crime_type_cols else None
main_area = area_cols[0] if area_cols else None
main_lat = next((col for col in location_cols if 'lat' in col), None)
main_lon = next((col for col in location_cols if 'lon' in col), None)

print(f"\nKey columns identified:")
print(f"Date: {main_date}, Crime Type: {main_crime_type}")
print(f"Area: {main_area}, Lat: {main_lat}, Lon: {main_lon}")

# Data cleaning
print("\nCleaning crime data...")

if main_date:
    crime_df['incident_date'] = pd.to_datetime(crime_df[main_date], errors='coerce')
    crime_df['year'] = crime_df['incident_date'].dt.year
    crime_df['month'] = crime_df['incident_date'].dt.month
    crime_df['day_of_week'] = crime_df['incident_date'].dt.day_name()

if main_crime_type:
    crime_df['crime_category'] = crime_df[main_crime_type].str.strip().str.title()

# Filter for recent data and valid locations
if main_lat and main_lon:
    valid_crimes = crime_df.dropna(subset=[main_lat, main_lon]).copy()
    valid_crimes = valid_crimes[(valid_crimes[main_lat] != 0) & (valid_crimes[main_lon] != 0)]
else:
    valid_crimes = crime_df.copy()

if 'year' in valid_crimes.columns:
    recent_crimes = valid_crimes[valid_crimes['year'] >= valid_crimes['year'].max() - 1]
else:
    recent_crimes = valid_crimes

print(f"Working with {len(recent_crimes):,} recent crime records")

# Basic crime statistics
print(f"\nCrime Data Overview:")
print(f"Total records: {len(crime_df):,}")
print(f"Date range: {crime_df['incident_date'].min()} to {crime_df['incident_date'].max()}")

if 'crime_category' in crime_df.columns:
    top_crimes = crime_df['crime_category'].value_counts().head(10)
    print(f"\nTop 10 crime types:")
    for crime, count in top_crimes.items():
        print(f"  {crime}: {count:,}")

# Time-based analysis
plt.figure(figsize=(15, 10))

# Monthly crime trends
plt.subplot(2, 2, 1)
if 'month' in crime_df.columns:
    monthly_crimes = crime_df['month'].value_counts().sort_index()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.plot(months, monthly_crimes.values, marker='o', linewidth=2)
    plt.title('Monthly Crime Distribution', fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('Number of Crimes')
    plt.grid(True, alpha=0.3)

# Daily crime patterns
plt.subplot(2, 2, 2)
if 'day_of_week' in crime_df.columns:
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_crimes = crime_df['day_of_week'].value_counts().reindex(day_order)
    plt.bar(range(len(daily_crimes)), daily_crimes.values, color='lightcoral')
    plt.title('Crimes by Day of Week', fontweight='bold')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Crimes')
    plt.xticks(range(len(daily_crimes)), [d[:3] for d in day_order])

# Crime type distribution
plt.subplot(2, 2, 3)
if 'crime_category' in crime_df.columns:
    top_10_crimes = crime_df['crime_category'].value_counts().head(10)
    plt.barh(range(len(top_10_crimes)), top_10_crimes.values, color='lightseagreen')
    plt.title('Top 10 Crime Types', fontweight='bold')
    plt.xlabel('Number of Incidents')
    plt.yticks(range(len(top_10_crimes)), top_10_crimes.index, fontsize=9)

# Yearly trend
plt.subplot(2, 2, 4)
if 'year' in crime_df.columns:
    yearly_trend = crime_df['year'].value_counts().sort_index()
    plt.plot(yearly_trend.index, yearly_trend.values, marker='s', color='purple', linewidth=2)
    plt.title('Crime Trend Over Years', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('crime_temporal_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Geospatial analysis
print("\nCreating crime maps...")

if main_lat and main_lon and len(recent_crimes) > 0:
    # Calculate center of crime data for map
    center_lat = recent_crimes[main_lat].mean()
    center_lon = recent_crimes[main_lon].mean()
    
    # Create base map
    crime_map = folium.Map(location=[center_lat, center_lon], zoom_start=11)
    
    # Add heatmap
    heat_data = [[row[main_lat], row[main_lon]] for _, row in recent_crimes.iterrows() if not pd.isna(row[main_lat]) and not pd.isna(row[main_lon])]
    HeatMap(heat_data, radius=15, blur=10, max_zoom=13).add_to(crime_map)
    
    # Save interactive map
    crime_map.save('crime_heatmap.html')
    print("Interactive heatmap saved as 'crime_heatmap.html'")
    
    # Create cluster map for specific crime types
    if 'crime_category' in recent_crimes.columns:
        violent_crimes = recent_crimes[recent_crimes['crime_category'].str.contains('assault|robbery|homicide|battery', case=False, na=False)]
        if len(violent_crimes) > 0:
            violent_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)
            
            for _, crime in violent_crimes.iterrows():
                folium.CircleMarker(
                    location=[crime[main_lat], crime[main_lon]],
                    radius=3,
                    color='red',
                    fill=True,
                    fill_color='red',
                    popup=f"{crime.get('crime_category', 'Unknown')}"
                ).add_to(violent_map)
            
            violent_map.save('violent_crimes_map.html')
            print("Violent crimes map saved as 'violent_crimes_map.html'")

# Area-based analysis
if main_area and main_area in crime_df.columns:
    print(f"\nCrime by Area Analysis:")
    area_crimes = crime_df[main_area].value_counts().head(10)
    
    plt.figure(figsize=(12, 6))
    area_crimes.plot(kind='bar', color='steelblue')
    plt.title('Top 10 Areas by Crime Count', fontweight='bold')
    plt.xlabel('Area')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('crime_by_area.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    for area, count in area_crimes.head(5).items():
        print(f"  {area}: {count:,} crimes")

# Answer key questions
print("\n" + "="*50)
print("KEY FINDINGS")
print("="*50)

# Question 1: Which areas have the highest crime rates?
print("\n1. HIGHEST CRIME AREAS:")
if main_area and main_area in crime_df.columns:
    area_stats = crime_df[main_area].value_counts().head(5)
    for i, (area, count) in enumerate(area_stats.items(), 1):
        print(f"  {i}. {area}: {count:,} incidents")
else:
    print("  No area data available")

# Question 2: Has crime increased or decreased?
print("\n2. CRIME TREND ANALYSIS:")
if 'year' in crime_df.columns:
    yearly_counts = crime_df['year'].value_counts().sort_index()
    if len(yearly_counts) > 1:
        current_year = yearly_counts.index.max()
        previous_year = yearly_counts.index[-2] if len(yearly_counts) > 1 else yearly_counts.index[-1]
        
        current_count = yearly_counts[current_year]
        previous_count = yearly_counts[previous_year]
        
        change = current_count - previous_count
        change_pct = (change / previous_count) * 100
        
        trend = "increased" if change > 0 else "decreased"
        print(f"  Crime has {trend} by {abs(change):,} incidents ({abs(change_pct):.1f}%)")
        print(f"  {previous_year}: {previous_count:,} crimes")
        print(f"  {current_year}: {current_count:,} crimes")
    else:
        print("  Insufficient data for trend analysis")
else:
    print("  No year data for trend analysis")

# Crime hotspots analysis
print("\n3. CRIME HOTSPOTS:")
if main_lat and main_lon and len(recent_crimes) > 0:
    # Simple grid-based hotspot detection
    recent_crimes['lat_round'] = recent_crimes[main_lat].round(2)
    recent_crimes['lon_round'] = recent_crimes[main_lon].round(2)
    
    hotspots = recent_crimes.groupby(['lat_round', 'lon_round']).size().nlargest(5)
    print("  Top 5 crime hotspots (approximate coordinates):")
    for (lat, lon), count in hotspots.items():
        print(f"  Location ({lat}, {lon}): {count} incidents")

# Time patterns
print("\n4. TIME PATTERNS:")
if 'day_of_week' in crime_df.columns:
    busiest_day = crime_df['day_of_week'].value_counts().idxmax()
    busiest_count = crime_df['day_of_week'].value_counts().max()
    print(f"  Busiest day: {busiest_day} ({busiest_count:,} incidents)")

if 'month' in crime_df.columns:
    busiest_month = crime_df['month'].value_counts().idxmax()
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][busiest_month - 1]
    print(f"  Busiest month: {month_name}")

# Recommendations
print("\n" + "="*50)
print("RECOMMENDATIONS")
print("="*50)
print("1. Increase police patrols in high-crime areas identified in heatmaps")
print("2. Focus resources on most frequent crime types")
print("3. Implement targeted interventions on peak crime days/times")
print("4. Use trend data for resource allocation planning")
print("5. Consider community programs in persistent hotspot areas")

print("\nCrime analysis completed!")