import os
import csv
import re


def read_episodes_file(file):
    data_list = {}
    try:
        with open(file, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader, None)
            if header:
                pass
            
            for row_num, row in enumerate(csv_reader, 1):
                dict_entry = {}
                dict_entry["entry"] = row_num
                dict_entry["season"] = row[0][1:3]
                dict_entry["episode"] = row[0][4:6]
                dict_entry["title"] = row[1]
                dict_entry["airdate"] = row[2]
                dict_entry["runtime"] = row[3]
                data_list[re.sub(r'[^\w]', '', row[1]).lower()] = dict_entry
        
        return data_list
    
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_csv_files(episodes):
    headers = ['id', 'speaker', 'speech', 'context', 'raw-dialouge', 'season', 'episode', 'title', 'airdate', 'runtime']
    data = []
    id = -1
    try:
        for filename in os.listdir("./SpongeBob_SquarePants_Transcripts"):
            file_path = os.path.join("./SpongeBob_SquarePants_Transcripts", filename)
            name = filename.replace(".txt", "").lower()
            if name not in episodes:
                continue
            episode_data = episodes[name]
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and line[0] != "[" and line[0] != "(" and line[0] != "♪":
                        speaker = line.split(":", 1)[0]
                        speaker = ''.join(re.split(r'\[.*?\]', speaker))
                        dialouge = line.split(":", 1)[1].strip()
                        context = ' '.join(re.findall(r'\[(.*?)\]', dialouge))
                        speech = ''.join(re.split(r'\[.*?\]', dialouge))
                        id += 1
                        data.append([str(id), speaker, speech, context, dialouge, episode_data["season"], episode_data["episode"], episode_data["title"], episode_data["airdate"], episode_data["runtime"]])

        with open("complete.csv", 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(headers)
            csv_writer.writerows(data)
        
        seasons = {
            '01': [],
            '02': [],
            '03': [],
            '04': [],
            '05': [],
            '06': [],
            '07': [],
            '08': [],
            '09': [],
            '10': [],
        }
        for entry in data:
            seasons[entry[5]].append(entry)
        
        for key, value in seasons.items():
            with open(f"season{key}.csv", 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(headers)
                csv_writer.writerows(value)
                
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    episodes_file = "SpongeBobEpisodes.csv"
    episodes_data = read_episodes_file(episodes_file)
    if episodes_data:
        generate_csv_files(episodes_data)