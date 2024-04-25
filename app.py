import streamlit as st

# Emission factors
EMISSION_FACTORS = {
    "Virtual": {
        "Electricity": 0.20707,  # kg CO2e per kWh
        "Internet Provider": 3.7,
        "Web_Cluster_Servers": 1.0,
        "Personal Computers": 0.233,  # kg per CO2
        "Mobile Devices": 7.06,  # kg per CO2
    },
    "Physical": {
        "Air Travel": 0.254,
        "Car Travel": 0.164,  # kg CO2 per km
        "Accommodation": 5,  # kg CO2 per attendee
        "Commute": {  
            "Shuttle/Public Transport": 2.8,  # kg CO2 per km
            "Car": 2.4,  # kg CO2 per km
        }
    }
}

# Function to calculate emissions
@st.cache_data
def calculate_emissions(inputs, emissions):
    if inputs["event_type"] == "Physical":
        total_emissions = (
            emissions["Air Travel"] * inputs["air_travel_distance"] +
            emissions["Car Travel"] * inputs["car_travel_distance"] +
            emissions["Accommodation"] * inputs["accommodation"] * inputs["participants"] +
            emissions["Commute"][inputs["commute_method"]] * inputs["commute_distance"]
        )
    else:
        total_emissions = (
            emissions["Electricity"] * inputs["electricity_consumption"] +
            emissions["Internet Provider"] * inputs["internet_provider"] +
            emissions["Web_Cluster_Servers"] * inputs["web_cluster_servers"] +
            emissions["Personal Computers"] * inputs["personal_computers"] +
            emissions["Mobile Devices"] * inputs["mobile_devices"]
        )
    return total_emissions

# Streamlit app code
st.title("Carbon Calculator")

# User inputs
st.subheader("Select Event Type")
event_type = st.radio("Event Type", ["Physical", "Virtual"])

# Initialize inputs dictionary
@st.cache_data  # Cache the input widget generation
def get_inputs():
    return {
        "event_type": "Physical",
        "air_travel_distance": 1000.0,
        "car_travel_distance": 1000.0,
        "accommodation": 0,
        "participants": 0,
        "commute_method": "",
        "commute_distance": 1000.0,
        "electricity_consumption": 1000.0,
        "internet_provider": 0.0,
        "web_cluster_servers": 0.0,
        "personal_computers": 0.0,
        "mobile_devices": 0.0
    }

inputs = get_inputs()

# Calculate emissions automatically as the user inputs data
emissions = EMISSION_FACTORS[event_type]

st.subheader("Emission Factors")
for factor, value in emissions.items():
    st.write(f"{factor}: {value}")

if event_type == "Physical":
    inputs["air_travel_distance"] = st.number_input("Air Travel Distance (km)", value=inputs["air_travel_distance"])
    inputs["car_travel_distance"] = st.number_input("Car Travel Distance (km)", value=inputs["car_travel_distance"])
    inputs["accommodation"] = st.number_input("Accommodation (attendees)", value=inputs["accommodation"])
    inputs["participants"] = st.number_input("Number of Participants", value=inputs["participants"])
    inputs["commute_method"] = st.radio("Commute Method", list(emissions["Commute"].keys()), index=0 if not inputs["commute_method"] else list(emissions["Commute"].keys()).index(inputs["commute_method"]))
    inputs["commute_distance"] = st.number_input(f"{inputs['commute_method']} Distance (km)", value=inputs["commute_distance"])

else:
    inputs["electricity_consumption"] = st.number_input("Electricity Consumption (kWh)", value=inputs["electricity_consumption"])
    inputs["internet_provider"] = st.number_input("Internet Provider Emissions", value=inputs["internet_provider"])
    inputs["web_cluster_servers"] = st.number_input("Web Cluster Servers Emissions", value=inputs["web_cluster_servers"])
    inputs["personal_computers"] = st.number_input("Personal Computers Emissions", value=inputs["personal_computers"])
    inputs["mobile_devices"] = st.number_input("Mobile Devices Emissions", value=inputs["mobile_devices"])

# Calculate emissions using the cached function
emissions_result = calculate_emissions(inputs, emissions)

# Display emissions
st.subheader("Total Emissions")
st.write(f"Total: {emissions_result:.2f} kg CO2")

st.image("images/king.jpg")
st.subheader("Rimba Raya Biodiversity Reserve")
st.divider()
st.image("images/queen.jpg")
st.subheader("Eden Reforestation")
st.divider()
st.image("images/pawn.jpg")
st.subheader("Second Life Ocean Plastic Recovery and Recycling")

