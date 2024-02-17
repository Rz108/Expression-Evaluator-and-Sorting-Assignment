# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement the report
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: report.py
#
#
# ------------------------------------------------------------


# Creating the report class
class Report:

    '''
    Creating the init here for each of the requried attributes
    '''
    def __init__(self, exp, idv_mean_time, idv_std_time, idv_median_time ):
        self.exp = exp
        self.max_expressions = 20
        self.pageIndex = 0
        self.itemsPerPage = 10
        self.idv_mean_time = idv_mean_time
        self.idv_std_time = idv_std_time
        self.idv_median_time = idv_median_time
    
    '''
    Setting the display page here
    '''
    def __display_page(self):

        # Setting the start index and the end index here and the number of items in a page
        startIdx = self.pageIndex * self.itemsPerPage
        endIdx = startIdx + self.itemsPerPage

        # Determine the title here
        title = ("Index\tExpression\t\t\tResult")
        print(title)
        print('_'*53)

        # Putting each expression togther with its index and mean time
        indexed_datas = [(i, self.exp[i], self.idv_mean_time[i]) for i in range(len(self.exp))]
        
        # Sorting the data by the mean time, descending
        sorted_datas = sorted(indexed_datas, key=lambda item: item[2], reverse=True)

        # Getting the page items here
        pageItems = sorted_datas[startIdx:endIdx]

        # Generating the values with key information here
        for item in pageItems:
            original_index, expr, mean_time = item
            exp_display = (expr[:27] + '...') if len(expr) > 30 else expr
            mean_time_rounded = round(mean_time, 6)
            print(f"|{str(original_index).ljust(6)}{exp_display.ljust(36)}{str(mean_time_rounded).ljust(9)}", ' '*(5 - len(str(mean_time_rounded))) + '|')  
        
        # Generating the end of the table here
        print('|' + '_'*52 + '|')

        # Getting the total page here
        total_pages = (len(self.exp) - 1) // self.itemsPerPage + 1

        # Print the page number here
        print(f"\nPage {self.pageIndex + 1} of {total_pages}")
        # Return the original indices of items in the current page
        return [item[0] for item in pageItems]

    '''
     This is to analyse expression further 
     ''' 
    def __analyse_exp(self, selectedIdx):
            
        # Get the selected expression here base on the start index
        selected_expr = self.exp[selectedIdx]

        # Print the selected expression here
        print(f"\nSelected Expression: {selected_expr}")

        # Getting the different statistics here
        avg_result = self.idv_mean_time[selectedIdx]
        std_dev = self.idv_std_time[selectedIdx]
        median_result = self.idv_median_time[selectedIdx]

        # Printint the different metrics here
        print(f"\nAverage Time Taken: {avg_result}s")
        print(f"Median Time Taken: {median_result}s")
        print(f"Standard Deviation Taken: {std_dev}s")

    '''
    getting the next page here base on the page index 
    ''' 
    def __next_page(self):
        if (self.pageIndex + 1) * self.itemsPerPage < len(self.exp):
            self.pageIndex += 1
            page_items = self.get_page()
            return page_items
        else:
            print("You are on the last page.")
    
    '''
    Getting the previous page here
    '''
    def __previous_page(self):
        if self.pageIndex > 0:
            self.pageIndex -= 1
            page_items = self.get_page()
            return page_items
        else:
            print("You are on the first page.")

    '''Getter here'''
    def get_page(self):
        return self.__display_page()
    
    def get_next_page(self):
        return self.__next_page()
    
    def get_previous_page(self):
        return self.__previous_page()
    
    '''Run the menu here'''
    def run_menu(self):
        page_items = self.get_page()
        try:
                
            # Getting the option for each page
            while True:
                print("\nOptions:")
                print("\t[n] Next Page")
                print("\t[p] Previous Page")
                print("\t[i] Analyze Individual Expression")
                print("\t[q] Quit Detailed Report")

                choice = input("\nEnter your choice: ").lower()

                # Asking the user to select the options
                if choice.lower() == 'n':
                    page_items = self.__next_page()
                elif choice.lower() == 'p':
                    page_items = self.__previous_page()
                elif choice.lower() == 'i':

                    # Validate that the input index is accurate and inside the page
                    try:
                        selectedIdx = int(input("\nEnter the index for further insights ('r' to return): "))
                        if str(selectedIdx).lower() == 'r':
                            continue
                        if selectedIdx in page_items:
                            self.__analyse_exp(selectedIdx)
                        
                        # Provide error message here 
                        else:
                            print("Invalid index. Please enter a valid index within the displayed page range.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                elif choice == 'q':
                    break
                else:
                    print("Invalid Input")
        except Exception as e:
            print(e)