import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
from persim.persistent_entropy import persistent_entropy

import gc  # Import garbage collection

# Parent directory containing folders with Excel files for each image
excel_folders_parent_dir = "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Point Cloud\\Normal cases\\"

# Parent directory for entropy folders
entropy_parent_folder = "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Entropy code\\3000\\Entropy\\Normal cases\\"

i = 0

# Iterate over each folder containing Excel files (each folder corresponds to an image)
for image_folder_name in os.listdir(excel_folders_parent_dir):
    image_folder_path = os.path.join(excel_folders_parent_dir, image_folder_name)
    if os.path.isdir(image_folder_path):
        print(f"Processing image folder: {image_folder_name}")

        # Create output folder for persistence diagrams
        output_folder_path = os.path.join(
            "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Persistence\\Normal cases\\",
            image_folder_name,
        )
        os.makedirs(output_folder_path, exist_ok=True)

        # Get a list of all Excel files in the directory (point cloud for the current image)
        excel_files = [
            file for file in os.listdir(image_folder_path) if file.endswith(".xlsx")
        ]

        # List to store entropy values for the current image
        image_entropy_values = []

        # Process each Excel file (each file represents a point cloud for the image)
        for excel_file in excel_files:
            excel_file_path = os.path.join(image_folder_path, excel_file)
            # Read the coordinates from the Excel file
            df = pd.read_excel(excel_file_path)
            data_array = df.iloc[:, :2].values

            # Compute persistence diagrams
            try:
                res = ripser(data_array, n_perm=3000, maxdim=1)
            except:
                try:
                    res = ripser(data_array, maxdim=1)
                except:
                    print("Skipping")
                    continue

            dgms_sub = res["dgms"]
            e0 = persistent_entropy(dgms_sub[0])
            e1 = persistent_entropy(dgms_sub[1])
            image_entropy_values.append((excel_file.split(".")[0], e0[0], e1[0]))

            # Plot and save persistence diagrams
            # plt.figure(figsize=(4, 4))
            # plot_diagrams(dgms_sub)
            # plt.title("Subsampled point's persistence diagrams")
            # output_file_path = os.path.join(output_folder_path, f'{os.path.splitext(excel_file)[0]}.png')
            # plt.savefig(output_file_path)
            # plt.close()

            # Clear large variables and force garbage collection after each file processing
            del df, data_array, res, dgms_sub, e0, e1
            gc.collect()

        # Create a DataFrame from the entropy values for the current image
        entropy_df = pd.DataFrame(
            columns=["Intensity", "Entropy 0", "Entropy 1"], data=image_entropy_values
        )

        # Save the DataFrame to an Excel file
        entropy_excel_file_path = os.path.join(
            entropy_parent_folder, f"{image_folder_name}_Entropy_values.xlsx"
        )
        entropy_df.to_excel(entropy_excel_file_path, index=False)
        # print(f"Entropy values for image {image_folder_name} saved to: {entropy_excel_file_path}")

        # Clear large variables and force garbage collection after each folder processing
        del image_entropy_values, entropy_df
        gc.collect()


# import os
# import time
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from ripser import ripser
# from persim import plot_diagrams
# from persim.persistent_entropy import persistent_entropy
# import gc  # Import garbage collection

# # Parent directory containing folders with Excel files for each image
# excel_folders_parent_dir = "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Point Cloud\\Bengin cases\\"

# # Parent directory for entropy folders
# entropy_parent_folder = "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Entropy code\\3000\\Entropy\\Bengin cases\\"
# i = 0

# # Iterate over each folder containing Excel files (each folder corresponds to an image)
# for image_folder_name in os.listdir(excel_folders_parent_dir):
#     image_folder_path = os.path.join(excel_folders_parent_dir, image_folder_name)
#     if os.path.isdir(image_folder_path):
#         print(f"Processing image folder: {image_folder_name}")

#         # Create output folder for persistence diagrams
#         output_folder_path = os.path.join(
#             "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Persistence\\Bengin cases\\",
#             image_folder_name,
#         )
#         os.makedirs(output_folder_path, exist_ok=True)

#         # Get a list of all Excel files in the directory (point cloud for the current image)
#         excel_files = [
#             file for file in os.listdir(image_folder_path) if file.endswith(".xlsx")
#         ]

#         # List to store entropy values for the current image
#         image_entropy_values = []

#         # Process each Excel file (each file represents a point cloud for the image)
#         for excel_file in excel_files:
#             excel_file_path = os.path.join(image_folder_path, excel_file)
#             # Read the coordinates from the Excel file
#             df = pd.read_excel(excel_file_path)
#             data_array = df.iloc[:, :2].values

#             # Compute persistence diagrams
#             try:
#                 res = ripser(data_array, n_perm=3000, maxdim=1)
#             except:
#                 try:
#                     res = ripser(data_array, maxdim=1)
#                 except:
#                     print("Skipping")
#                     continue

#             dgms_sub = res["dgms"]
#             e0 = persistent_entropy(dgms_sub[0])
#             e1 = persistent_entropy(dgms_sub[1])
#             image_entropy_values.append((excel_file.split(".")[0], e0[0], e1[0]))

#             # Plot and save persistence diagrams
#             # plt.figure(figsize=(4, 4))
#             # plot_diagrams(dgms_sub)
#             # plt.title("Subsampled point's persistence diagrams")
#             # output_file_path = os.path.join(output_folder_path, f'{os.path.splitext(excel_file)[0]}.png')
#             # plt.savefig(output_file_path)
#             # plt.close()

#             # Clear large variables and force garbage collection after each file processing
#             del df, data_array, res, dgms_sub, e0, e1
#             gc.collect()

#         # Create a DataFrame from the entropy values for the current image
#         entropy_df = pd.DataFrame(
#             columns=["Intensity", "Entropy 0", "Entropy 1"], data=image_entropy_values
#         )

#         # Save the DataFrame to an Excel file
#         entropy_excel_file_path = os.path.join(
#             entropy_parent_folder, f"{image_folder_name}_Entropy_values.xlsx"
#         )
#         entropy_df.to_excel(entropy_excel_file_path, index=False)
#         # print(f"Entropy values for image {image_folder_name} saved to: {entropy_excel_file_path}")

#         # Clear large variables and force garbage collection after each folder processing
#         del image_entropy_values, entropy_df
#         gc.collect()


# import os
# import time
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from ripser import ripser
# from persim import plot_diagrams
# from persim.persistent_entropy import persistent_entropy
# import gc  # Import garbage collection

# # Parent directory containing folders with Excel files for each image
# excel_folders_parent_dir = "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Point Cloud\\Malignant cases\\"

# # Parent directory for entropy folders
# entropy_parent_folder = "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Entropy code\\3000\\Entropy\\Malignant cases\\"
# i = 0

# # Iterate over each folder containing Excel files (each folder corresponds to an image)
# for image_folder_name in os.listdir(excel_folders_parent_dir):
#     image_folder_path = os.path.join(excel_folders_parent_dir, image_folder_name)
#     if os.path.isdir(image_folder_path):
#         print(f"Processing image folder: {image_folder_name}")

#         # Create output folder for persistence diagrams
#         output_folder_path = os.path.join(
#             "C:\\Users\\Aneesh PB\\Downloads\\Topology Project\\Full segment\\Persistence\\Malignant cases\\",
#             image_folder_name,
#         )
#         os.makedirs(output_folder_path, exist_ok=True)

#         # Get a list of all Excel files in the directory (point cloud for the current image)
#         excel_files = [
#             file for file in os.listdir(image_folder_path) if file.endswith(".xlsx")
#         ]

#         # List to store entropy values for the current image
#         image_entropy_values = []

#         # Process each Excel file (each file represents a point cloud for the image)
#         for excel_file in excel_files:
#             excel_file_path = os.path.join(image_folder_path, excel_file)
#             # Read the coordinates from the Excel file
#             df = pd.read_excel(excel_file_path)
#             data_array = df.iloc[:, :2].values

#             # Compute persistence diagrams
#             try:
#                 res = ripser(data_array, n_perm=3000, maxdim=1)
#             except:
#                 try:
#                     res = ripser(data_array, maxdim=1)
#                 except:
#                     print("Skipping")
#                     continue

#             dgms_sub = res["dgms"]
#             e0 = persistent_entropy(dgms_sub[0])
#             e1 = persistent_entropy(dgms_sub[1])
#             image_entropy_values.append((excel_file.split(".")[0], e0[0], e1[0]))

#             # Plot and save persistence diagrams
#             # plt.figure(figsize=(4, 4))
#             # plot_diagrams(dgms_sub)
#             # plt.title("Subsampled point's persistence diagrams")
#             # output_file_path = os.path.join(output_folder_path, f'{os.path.splitext(excel_file)[0]}.png')
#             # plt.savefig(output_file_path)
#             # plt.close()

#             # Clear large variables and force garbage collection after each file processing
#             del df, data_array, res, dgms_sub, e0, e1
#             gc.collect()

#         # Create a DataFrame from the entropy values for the current image
#         entropy_df = pd.DataFrame(
#             columns=["Intensity", "Entropy 0", "Entropy 1"], data=image_entropy_values
#         )

#         # Save the DataFrame to an Excel file
#         entropy_excel_file_path = os.path.join(
#             entropy_parent_folder, f"{image_folder_name}_Entropy_values.xlsx"
#         )
#         entropy_df.to_excel(entropy_excel_file_path, index=False)
#         # print(f"Entropy values for image {image_folder_name} saved to: {entropy_excel_file_path}")

#         # Clear large variables and force garbage collection after each folder processing
#         del image_entropy_values, entropy_df
#         gc.collect()
