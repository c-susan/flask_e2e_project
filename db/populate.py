from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from create_table import geo_area_id
import os
import random 
from dotenv import load_dotenv

load_dotenv()

## Database credentials 
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string and creating the engine 
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")
engine = create_engine(
        connection_string,
        connect_args=connect_args)

# Creating a session to populate the data
Session = sessionmaker(bind=engine)
session = Session()

values = [
(1, "Borough", "Bronx"),
(1, "Borough", "New York City"),
(1, "Citywide", "Bronx"),
(1, "Citywide", "New York City"),
(2, "Borough", "Brooklyn"),
(3, "Borough", "Manhattan"),
(4, "Borough", "Queens"),
(5, "Borough", "Staten Island"),
(101, "CD", "Financial District (CD1)"),
(101, "CD", "Kingsbridge - Riverdale"),
(101, "UHF42", "Financial District (CD1)"),
(101, "UHF42", "Kingsbridge - Riverdale"),
(101, "UHF34", "Financial District (CD1)"),
(101, "UHF34", "Kingsbridge - Riverdale"),
(102, "CD", "Greenwich Village and Soho (CD2)"),
(102, "CD", "Northeast Bronx"),
(102, "UHF42", "Greenwich Village and Soho (CD2)"),
(102, "UHF42", "Northeast Bronx"),
(102, "UHF34", "Greenwich Village and Soho (CD2)"),
(102, "UHF34", "Northeast Bronx"),
(103, "UHF42", "Fordham - Bronx Pk"),
(103, "UHF42", "Lower East Side and Chinatown (CD3)"),
(103, "CD", "Fordham - Bronx Pk"),
(103, "CD", "Lower East Side and Chinatown (CD3)"),
(103, "UHF34", "Fordham - Bronx Pk"),
(103, "UHF34", "Lower East Side and Chinatown (CD3)"),
(104, "CD", "Clinton and Chelsea (CD4)"),
(104, "CD", "Pelham - Throgs Neck"),
(104, "UHF42", "Clinton and Chelsea (CD4)"),
(104, "UHF42", "Pelham - Throgs Neck"),
(104, "UHF34", "Clinton and Chelsea (CD4)"),
(104, "UHF34", "Pelham - Throgs Neck"),
(105, "UHF42", "Crotona -Tremont"),
(105, "UHF42", "Midtown (CD5)"),
(105, "CD", "Crotona -Tremont"),
(105, "CD", "Midtown (CD5)"),
(106, "UHF42", "High Bridge - Morrisania"),
(106, "UHF42", "Stuyvesant Town and Turtle Bay (CD6)"),
(106, "CD", "High Bridge - Morrisania"),
(106, "CD", "Stuyvesant Town and Turtle Bay (CD6)"),
(107, "UHF42", "Hunts Point - Mott Haven"),
(107, "UHF42", "Upper West Side (CD7)"),
(107, "CD", "Hunts Point - Mott Haven"),
(107, "CD", "Upper West Side (CD7)"),
(108, "CD", "Upper East Side (CD8)"),
(109, "CD", "Morningside Heights and Hamilton Heights (CD9)"),
(110, "CD", "Central Harlem (CD10)"),
(111, "CD", "East Harlem (CD11)"),
(112, "CD", "Washington Heights and Inwood (CD12)"),
(201, "UHF42", "Greenpoint"),
(201, "UHF42", "Mott Haven and Melrose (CD1)"),
(201, "CD", "Greenpoint"),
(201, "CD", "Mott Haven and Melrose (CD1)"),
(201, "UHF34", "Greenpoint"),
(201, "UHF34", "Mott Haven and Melrose (CD1)"),
(202, "UHF42", "Downtown - Heights - Slope"),
(202, "UHF42", "Hunts Point and Longwood (CD2)"),
(202, "CD", "Downtown - Heights - Slope"),
(202, "CD", "Hunts Point and Longwood (CD2)"),
(202, "UHF34", "Downtown - Heights - Slope"),
(202, "UHF34", "Hunts Point and Longwood (CD2)"),
(203, "UHF42", "Bedford Stuyvesant - Crown Heights"),
(203, "UHF42", "Morrisania and Crotona (CD3)"),
(203, "CD", "Bedford Stuyvesant - Crown Heights"),
(203, "CD", "Morrisania and Crotona (CD3)"),
(203, "UHF34", "Bedford Stuyvesant - Crown Heights"),
(203, "UHF34", "Morrisania and Crotona (CD3)"),
(204, "UHF42", "East New York"),
(204, "UHF42", "Highbridge and Concourse (CD4)"),
(204, "CD", "East New York"),
(204, "CD", "Highbridge and Concourse (CD4)"),
(204, "UHF34", "East New York"),
(204, "UHF34", "Highbridge and Concourse (CD4)"),
(205, "CD", "Fordham and University Heights (CD5)"),
(205, "CD", "Sunset Park"),
(205, "UHF42", "Fordham and University Heights (CD5)"),
(205, "UHF42", "Sunset Park"),
(205, "UHF34", "Fordham and University Heights (CD5)"),
(205, "UHF34", "Sunset Park"),
(206, "CD", "Belmont and East Tremont (CD6)"),
(206, "CD", "Borough Park"),
(206, "UHF42", "Belmont and East Tremont (CD6)"),
(206, "UHF42", "Borough Park"),
(206, "UHF34", "Belmont and East Tremont (CD6)"),
(206, "UHF34", "Borough Park"),
(207, "UHF42", "East Flatbush - Flatbush"),
(207, "UHF42", "Kingsbridge Heights and Bedford (CD7)"),
(207, "CD", "East Flatbush - Flatbush"),
(207, "CD", "Kingsbridge Heights and Bedford (CD7)"),
(207, "UHF34", "East Flatbush - Flatbush"),
(207, "UHF34", "Kingsbridge Heights and Bedford (CD7)"),
(208, "UHF42", "Canarsie - Flatlands"),
(208, "UHF42", "Riverdale and Fieldston (CD8)"),
(208, "CD", "Canarsie - Flatlands"),
(208, "CD", "Riverdale and Fieldston (CD8)"),
(208, "UHF34", "Canarsie - Flatlands"),
(208, "UHF34", "Riverdale and Fieldston (CD8)"),
(209, "UHF42", "Bensonhurst - Bay Ridge"),
(209, "UHF42", "Parkchester and Soundview (CD9)"),
(209, "CD", "Bensonhurst - Bay Ridge"),
(209, "CD", "Parkchester and Soundview (CD9)"),
(209, "UHF34", "Bensonhurst - Bay Ridge"),
(209, "UHF34", "Parkchester and Soundview (CD9)"),
(210, "UHF42", "Coney Island - Sheepshead Bay"),
(210, "UHF42", "Throgs Neck and Co-op City (CD10)"),
(210, "CD", "Coney Island - Sheepshead Bay"),
(210, "CD", "Throgs Neck and Co-op City (CD10)"),
(210, "UHF34", "Coney Island - Sheepshead Bay"),
(210, "UHF34", "Throgs Neck and Co-op City (CD10)"),
(211, "CD", "Morris Park and Bronxdale (CD11)"),
(211, "CD", "Williamsburg - Bushwick"),
(211, "UHF42", "Morris Park and Bronxdale (CD11)"),
(211, "UHF42", "Williamsburg - Bushwick"),
(211, "UHF34", "Morris Park and Bronxdale (CD11)"),
(211, "UHF34", "Williamsburg - Bushwick"),
(212, "CD", "Williamsbridge and Baychester (CD12)"),
(301, "CD", "Greenpoint and Williamsburg (CD1)"),
(301, "CD", "Washington Heights"),
(301, "UHF42", "Greenpoint and Williamsburg (CD1)"),
(301, "UHF42", "Washington Heights"),
(301, "UHF34", "Greenpoint and Williamsburg (CD1)"),
(301, "UHF34", "Washington Heights"),
(302, "UHF42", "Central Harlem - Morningside Heights"),
(302, "UHF42", "Fort Greene and Brooklyn Heights (CD2)"),
(302, "CD", "Central Harlem - Morningside Heights"),
(302, "CD", "Fort Greene and Brooklyn Heights (CD2)"),
(302, "UHF34", "Central Harlem - Morningside Heights"),
(302, "UHF34", "Fort Greene and Brooklyn Heights (CD2)"),
(303, "CD", "Bedford Stuyvesant (CD3)"),
(303, "CD", "East Harlem"),
(303, "UHF42", "Bedford Stuyvesant (CD3)"),
(303, "UHF42", "East Harlem"),
(303, "UHF34", "Bedford Stuyvesant (CD3)"),
(303, "UHF34", "East Harlem"),
(304, "CD", "Bushwick (CD4)"),
(304, "CD", "Upper West Side"),
(304, "UHF42", "Bushwick (CD4)"),
(304, "UHF42", "Upper West Side"),
(304, "UHF34", "Bushwick (CD4)"),
(304, "UHF34", "Upper West Side"),
(305, "CD", "East New York and Starrett City (CD5)"),
(305, "CD", "Upper East Side"),
(305, "UHF42", "East New York and Starrett City (CD5)"),
(305, "UHF42", "Upper East Side"),
(306, "UHF42", "Chelsea - Clinton"),
(306, "UHF42", "Park Slope and Carroll Gardens (CD6)"),
(306, "CD", "Chelsea - Clinton"),
(306, "CD", "Park Slope and Carroll Gardens (CD6)"),
(307, "UHF42", "Gramercy Park - Murray Hill"),
(307, "UHF42", "Sunset Park (CD7)"),
(307, "CD", "Gramercy Park - Murray Hill"),
(307, "CD", "Sunset Park (CD7)"),
(308, "CD", "Crown Heights and Prospect Heights (CD8)"),
(308, "CD", "Greenwich Village - SoHo"),
(308, "UHF42", "Crown Heights and Prospect Heights (CD8)"),
(308, "UHF42", "Greenwich Village - SoHo"),
(309, "CD", "South Crown Heights and Lefferts Gardens (CD9)"),
(309, "CD", "Union Square - Lower East Side"),
(309, "UHF42", "South Crown Heights and Lefferts Gardens (CD9)"),
(309, "UHF42", "Union Square - Lower East Side"),
(310, "CD", "Bay Ridge and Dyker Heights (CD10)"),
(310, "CD", "Lower Manhattan"),
(310, "UHF42", "Bay Ridge and Dyker Heights (CD10)"),
(310, "UHF42", "Lower Manhattan"),
(311, "CD", "Bensonhurst (CD11)"),
(312, "CD", "Borough Park (CD12)"),
(313, "CD", "Coney Island (CD13)"),
(314, "CD", "Flatbush and Midwood (CD14)"),
(315, "CD", "Sheepshead Bay (CD15)"),
(316, "CD", "Brownsville (CD16)"),
(317, "CD", "East Flatbush (CD17)"),
(318, "CD", "Flatlands and Canarsie (CD18)"),
(401, "UHF42", "Long Island City - Astoria"),
(401, "UHF42", "Long Island City and Astoria (CD1)"),
(401, "CD", "Long Island City - Astoria"),
(401, "CD", "Long Island City and Astoria (CD1)"),
(401, "UHF34", "Long Island City - Astoria"),
(401, "UHF34", "Long Island City and Astoria (CD1)"),
(402, "UHF42", "West Queens"),
(402, "UHF42", "Woodside and Sunnyside (CD2)"),
(402, "CD", "West Queens"),
(402, "CD", "Woodside and Sunnyside (CD2)"),
(402, "UHF34", "West Queens"),
(402, "UHF34", "Woodside and Sunnyside (CD2)"),
(403, "UHF42", "Flushing - Clearview"),
(403, "UHF42", "Jackson Heights (CD3)"),
(403, "CD", "Flushing - Clearview"),
(403, "CD", "Jackson Heights (CD3)"),
(403, "UHF34", "Flushing - Clearview"),
(403, "UHF34", "Jackson Heights (CD3)"),
(404, "UHF42", "Bayside - Little Neck"),
(404, "UHF42", "Elmhurst and Corona (CD4)"),
(404, "CD", "Bayside - Little Neck"),
(404, "CD", "Elmhurst and Corona (CD4)"),
(405, "UHF42", "Ridgewood - Forest Hills"),
(405, "UHF42", "Ridgewood and Maspeth (CD5)"),
(405, "CD", "Ridgewood - Forest Hills"),
(405, "CD", "Ridgewood and Maspeth (CD5)"),
(405, "UHF34", "Ridgewood - Forest Hills"),
(405, "UHF34", "Ridgewood and Maspeth (CD5)"),
(406, "UHF42", "Fresh Meadows"),
(406, "UHF42", "Rego Park and Forest Hills (CD6)"),
(406, "CD", "Fresh Meadows"),
(406, "CD", "Rego Park and Forest Hills (CD6)"),
(407, "CD", "Flushing and Whitestone (CD7)"),
(407, "CD", "Southwest Queens"),
(407, "UHF42", "Flushing and Whitestone (CD7)"),
(407, "UHF42", "Southwest Queens"),
(407, "UHF34", "Flushing and Whitestone (CD7)"),
(407, "UHF34", "Southwest Queens"),
(408, "CD", "Hillcrest and Fresh Meadows (CD8)"),
(408, "CD", "Jamaica"),
(408, "UHF42", "Hillcrest and Fresh Meadows (CD8)"),
(408, "UHF42", "Jamaica"),
(408, "UHF34", "Hillcrest and Fresh Meadows (CD8)"),
(408, "UHF34", "Jamaica"),
(409, "CD", "Kew Gardens and Woodhaven (CD9)"),
(409, "CD", "Southeast Queens"),
(409, "UHF42", "Kew Gardens and Woodhaven (CD9)"),
(409, "UHF42", "Southeast Queens"),
(409, "UHF34", "Kew Gardens and Woodhaven (CD9)"),
(409, "UHF34", "Southeast Queens"),
(410, "UHF42", "Rockaways"),
(410, "UHF42", "South Ozone Park and Howard Beach (CD10)"),
(410, "CD", "Rockaways"),
(410, "CD", "South Ozone Park and Howard Beach (CD10)"),
(410, "UHF34", "Rockaways"),
(410, "UHF34", "South Ozone Park and Howard Beach (CD10)"),
(411, "CD", "Bayside and Little Neck (CD11)"),
(412, "CD", "Jamaica and Hollis (CD12)"),
(413, "CD", "Queens Village (CD13)"),
(414, "CD", "Rockaway and Broad Channel (CD14)"),
(501, "UHF42", "Port Richmond"),
(501, "UHF42", "St. George and Stapleton (CD1)"),
(501, "CD", "Port Richmond"),
(501, "CD", "St. George and Stapleton (CD1)"),
(502, "CD", "South Beach and Willowbrook (CD2)"),
(502, "CD", "Stapleton - St. George"),
(502, "UHF42", "South Beach and Willowbrook (CD2)"),
(502, "UHF42", "Stapleton - St. George"),
(503, "CD", "Tottenville and Great Kills (CD3)"),
(503, "CD", "Willowbrook"),
(503, "UHF42", "Tottenville and Great Kills (CD3)"),
(503, "UHF42", "Willowbrook"),
(504, "UHF42", "South Beach - Tottenville"),
(305307, "UHF34", "Upper East Side-Gramercy"),
(306308, "UHF34", "Chelsea-Village"),
(309310, "UHF34", "Union Square-Lower Manhattan"),
(404406, "UHF34", "Bayside Little Neck-Fresh Meadows"),
(501502, "UHF34", "Northern SI"),
(503504, "UHF34", "Southern SI"),
(105106107, "UHF34", "South Bronx"),]

for geo_id, geo_type_name, geo_place_name in values:
    geo_area = geo_area_id(
        geo_id=geo_id,
        geo_type_name=geo_type_name,
        geo_place_name=geo_place_name
    )
    session.add(geo_area)


# Commit the changes to the database
session.commit()

# Close the session
session.close()