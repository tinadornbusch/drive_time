from driving_distance_calc import DrivingDistanceCalc
import pandas

END_ZIP = "19148"

# If some data has already been pulled, set starting_index to the index of the line you want to start on
starting_index = 0
total_data_points = 100

# Create zips_list
with open("spreadsheet_data.csv", mode="r") as data:
    data_frame = pandas.read_csv(data, converters={"zipcodes": str})
    zips_list = data_frame.zipcodes.tolist()

for zip_code_in_list in zips_list[starting_index:starting_index+total_data_points]:
    driving_calculator = DrivingDistanceCalc()
    drive_time = driving_calculator.calc_drive_time(zip_code_in_list,END_ZIP)

    # Extract integer in minutes of drive time between the two locations
    if len(drive_time) <= 6:
        drive_time_split = drive_time.split(sep=" ")
        drive_time_int = int(drive_time_split[0])
    else:
        drive_time_split = drive_time.split(sep=" ")
        drive_time_int = int(drive_time_split[0])*60 + int(drive_time_split[2])

    # Send data to the spreadsheet to record
    zip_index = zips_list.index(zip_code_in_list)
    data_frame.at[zip_index, "incoming"] = drive_time_int
    # interface.put_data(zip_code=zip_code_in_list, zip_code_index=zip_index+2, input_data=drive_time_int)

csv_data = data_frame.to_csv("spreadsheet_data_new.csv")
