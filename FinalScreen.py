import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup as BS
import UserInputManager as us
import json


def create_page(master):
    global final
    final = ttk.Frame(master, width=1000, height=750)
    final.columnconfigure(0, weight=2)
    final.columnconfigure(1, weight=2)
    final.columnconfigure(2, weight=2)
    final.rowconfigure(0, weight=2)
    final.rowconfigure(1, weight=2)
    final.rowconfigure(2, weight=2)
    tk.Button(final, text='Restart', bg='#8B2323', command=None).grid(row=2, column=0, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(final, text='EXIT', bg='#8B2323',
              command=popup_check).grid(row=2, column=2, sticky=tk.E, padx=15, ipadx=15)
    return final


def popup_check():
    pop = tk.Toplevel()
    pop.wm_title("Exit: Warning.")
    msg = tk.Label(pop, text='Are you sure you want to exit? No progress will manually be saved for this assessment.')
    msg.grid(row=0, column=0, sticky=tk.E, columnspan=2)
    yes_btn = tk.Button(pop, text='YES', bg='light green', command=lambda: [pop.destroy(), final.destroy()])
    yes_btn.grid(row=1, column=0, sticky=tk.E, padx=15)
    no_btn = tk.Button(pop, text='NO', bg='red', command=pop.destroy)
    no_btn.grid(row=1, column=1, sticky=tk.W)


def create_rula_assessment_report(all_user_info):
    user_input = all_user_info[0]
    image_selections = all_user_info[1]
    adjustment_selections = all_user_info[2]
    # text_boxes = all_user_info[3]
    #
    name = user_input[0]
    task_name = user_input[1]
    date = user_input[2]

    rula_tables = us.RulaTableManager()

    with open('templates/rula-assessment-report.html') as h:
        soup = BS(h, 'html.parser')

        # User Input
        info = soup.find(id="revInfo")
        ans1 = soup.find(id="answer1")
        ans2 = soup.find(id="answer2")
        ans3 = soup.find(id="answer3")
        ans4 = soup.find(id="answer4")
        ans5 = soup.find(id="answer5")
        ans6 = soup.find(id="answer6")
        ans7 = soup.find(id="answer7")
        ans8 = soup.find(id="answer8")
        ans9 = soup.find(id="answer9")
        ans10 = soup.find(id="answer10")
        ans11 = soup.find(id="answer11")
        ans12 = soup.find(id="answer12")
        ans13 = soup.find(id="answer13")
        ans14 = soup.find(id="answer14")
        ans15 = soup.find(id="answer15")
        final_score = soup.find(id="finalScore")

        info.string = name + "    " + task_name + "    " + date
        ans1_val = image_selections[0] + adjustment_selections[0]
        ans2_val = image_selections[1] + adjustment_selections[1]
        ans3_val = image_selections[2] + adjustment_selections[2]
        ans4_val = image_selections[3]
        ans5_val = rula_tables.get_tableA_score(ans3_val, ans1_val, ans2_val, ans4_val)
        ans6_val = adjustment_selections[3]
        ans7_val = adjustment_selections[4]
        ans8_val = ans5_val + ans6_val + ans7_val
        ans9_val = image_selections[4] + adjustment_selections[5]
        ans10_val = image_selections[5] + adjustment_selections[6]
        ans11_val = image_selections[6]
        ans12_val = rula_tables.get_tableB_score(ans10_val, ans9_val, ans11_val)
        ans13_val = adjustment_selections[7]
        ans14_val = adjustment_selections[8]
        ans15_val = ans12_val + ans13_val + ans14_val
        final_val = rula_tables.get_tableC_score(ans15_val, ans8_val)

        ans1.string = str(ans1_val)
        ans2.string = str(ans2_val)
        ans3.string = str(ans3_val)
        ans4.string = str(ans4_val)
        ans5.string = str(ans5_val)
        ans6.string = str(ans6_val)
        ans7.string = str(ans7_val)
        ans8.string = str(ans8_val)
        ans9.string = str(ans9_val)
        ans10.string = str(ans10_val)
        ans11.string = str(ans11_val)
        ans12.string = str(ans12_val)
        ans13.string = str(ans13_val)
        ans14.string = str(ans14_val)
        ans15.string = str(ans15_val)
        final_score.string = str(final_val)

        with open('templates/rula-assessment-report.html', "w") as t:
            t.write(soup.prettify())


def create_reba_assessment_report(all_user_info):
    user_input = all_user_info[0]
    image_selections = all_user_info[1]
    adjustment_selections = all_user_info[2]
    # text_boxes = all_user_info[3]
    #
    name = user_input[0]
    task_name = user_input[1]
    date = user_input[2]

    reba_tables = us.RebaTableManager()

    with open('templates/reba-assessment-report.html') as h:
        soup = BS(h, 'html.parser')

        # User Input
        info = soup.find(id="revInfo")
        ans1 = soup.find(id="answer1")
        ans2 = soup.find(id="answer2")
        ans3 = soup.find(id="answer3")
        ans4 = soup.find(id="answer4")
        ans5 = soup.find(id="answer5")
        ans6 = soup.find(id="answer6")
        ans7 = soup.find(id="answer7")
        ans8 = soup.find(id="answer8")
        ans9 = soup.find(id="answer9")
        ans10 = soup.find(id="answer10")
        ans11 = soup.find(id="answer11")
        ans12 = soup.find(id="answer12")
        table_c_score = soup.find(id="valueC")
        activity_score = soup.find(id="actScore")
        final_score = soup.find(id="finalScore")

        info.string = name + "    " + task_name + "    " + date
        ans1_val = image_selections[0] + adjustment_selections[0]
        ans2_val = image_selections[1] + adjustment_selections[1]
        ans3_val = image_selections[2] + adjustment_selections[2]
        ans4_val = reba_tables.get_tableA_score(ans1_val, ans2_val, ans3_val, 0)
        ans5_val = adjustment_selections[3]
        ans6_val = ans4_val + ans5_val
        ans7_val = image_selections[3] + adjustment_selections[4]
        ans8_val = image_selections[4]
        ans9_val = image_selections[5] + adjustment_selections[5]
        ans10_val = reba_tables.get_tableB_score(ans8_val, ans7_val, ans9_val)
        ans11_val = adjustment_selections[6]
        ans12_val = ans10_val + ans11_val
        table_c_val = reba_tables.get_tableC_score(ans6_val, ans12_val)
        active_val = adjustment_selections[7]
        final_val = table_c_val + active_val

        ans1.string = str(ans1_val)
        ans2.string = str(ans2_val)
        ans3.string = str(ans3_val)
        ans4.string = str(ans4_val)
        ans5.string = str(ans5_val)
        ans6.string = str(ans6_val)
        ans7.string = str(ans7_val)
        ans8.string = str(ans8_val)
        ans9.string = str(ans9_val)
        ans10.string = str(ans10_val)
        ans11.string = str(ans11_val)
        ans12.string = str(ans12_val)
        table_c_score.string = str(table_c_val)
        activity_score.string = str(active_val)
        final_score.string = str(final_val)

        with open('templates/reba-assessment-report.html', "w") as t:
            t.write(soup.prettify())
