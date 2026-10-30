import openpyxl
import os

def mea(file_path):
    # Load the workbook
    wb = openpyxl.load_workbook(file_path)
    
    # Get the first sheet
    sheet = wb.active
    
    # Extract column D
    column_d = []
    for cell in sheet['D:D']:
        if cell.value is not None:
            column_d.append(cell.value)
    
    # Extract column A
    column_a = []
    for cell in sheet['A:A']:
        if cell.value is not None:
            column_a.append(cell.value)
    
    return column_d, column_a

# Example usage
if __name__ == "__main__":
    # Use relative path to data directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "X-Challenge 2026 Tesztforduló_Poople_Tesztforduló_B.xlsx")
    column_d, column_a = mea(file_path)
    print("Column D:", column_d)
    #print("Column A:", column_a)