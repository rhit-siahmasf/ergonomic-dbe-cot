# NECK, LEG, & TRUNK screens
# b_trunk_title = sm.LabelWidget(master, 'B. NECK, TRUNK, AND LEG ANALYSIS', 0, 0, default_font, 18, tk.W)
# # Step B6 -----------------------------------------------------------------------------------------------
# # -------------------- OPTIONS B6 --------------------------------------------------
# b6_step_options = [sm.CheckButtonWidget(master, option_type, 'If load < 4.4 lbs (intermittent): (+0)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If load 4.4 to 22 lbs (intermittent): (+1)', 1, 1, tk.S),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If load 4.4 to 22 lbs (static or repeated): (+2)', 2, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If more than 22lbs OR repeated or shocks: (+3)', 2, 1, tk.S)]
# # --------------------- TITLE B6 ---------------------------------------------------
# b6_title = sm.LabelWidget(master, 'Step 14: Add Force / Load Score', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B6 ---------------------------------------------------
# b6_step_screen = sm.ScreenManager(master, b_trunk_title, b6_title, [], b6_step_options, all_others, None, None)
# # Step B5 -----------------------------------------------------------------------------------------------
# b5_option = [sm.CheckButtonWidget(master, option_type,
#                                   'Action repeated occurs 4x/minute? '
#                                   'OR is posture mainly static (i.e held >10 minutes)? (+1)', 4, 1, tk.N)]
# b5_title = sm.LabelWidget(master, 'Step 13: Add Muscle Score.', 4, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B5 ---------------------------------------------------
# b5_step_screen = sm.ScreenManager(master, '', b5_title, [], b5_option, [], None, b6_step_screen)
# # Step B4-----------------------------------------------------------------------------------------------
# b4_title = sm.LabelWidget(master, 'Step 12: Posture Score from Table.', 3, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B4 ---------------------------------------------------
# b4_step_screen = sm.ScreenManager(master, '', b4_title, [], [], [], None, b5_step_screen)
# # Step B3 -----------------------------------------------------------------------------------------------
# b3_step_options = [sm.CheckButtonWidget(master, option_type, 'If legs and feet are supported: (+1)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If NOT supported: (+2)', 1, 1, tk.S)]
# b3_title = sm.LabelWidget(master, 'Step 11: Legs.', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B3 ---------------------------------------------------
# b3_step_screen = sm.ScreenManager(master, b_trunk_title, b3_title, [], b3_step_options, [], None, b4_step_screen)
# # Step B2 -----------------------------------------------------------------------------------------------
# # -------------------- IMAGES B2 --------------------------------------------------
# b2_step_images = [sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-1.png'),
#                                  img_type, 0, 1, tk.W),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-2.png'),
#                                  img_type, 0, 1, tk.NSEW),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-3.png'),
#                                  img_type, 0, 1, tk.E),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-4.png'),
#                                  img_type, 1, 1, tk.W)]
# # -------------------- OPTIONS B2 --------------------------------------------------
# b2_step_options = [sm.CheckButtonWidget(master, option_type, 'Adjust if trunk is twisted: (+1)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'Adjust if trunk is side bending: (+1)', 1, 1, tk.S)]
# # --------------------- TITLE B2 ---------------------------------------------------
# b2_title = sm.LabelWidget(master, 'Step 10: Locate Trunk Position.', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B2 ---------------------------------------------------
# b2_step_screen = sm.ScreenManager(master, b_trunk_title, b2_title, b2_step_images,
#                                   b2_step_options, all_others, None, b3_step_screen)
# # Step B1 -----------------------------------------------------------------------------------------------
# # -------------------- IMAGES B1 --------------------------------------------------
# b1_step_images = [sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-1.png'),
#                                  img_type, 0, 1, tk.W),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-2.png'),
#                                  img_type, 0, 1, tk.NSEW),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-3.png'),
#                                  img_type, 0, 1, tk.E),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-4.png'),
#                                  img_type, 1, 1, tk.W)]
# # -------------------- OPTIONS B1 --------------------------------------------------
# b1_step_options = [sm.CheckButtonWidget(master, option_type, 'Adjust if neck is twisted: (+1)', 2, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'Adjust if neck is side bending: (+1)', 2, 1, tk.S)]
# # --------------------- TITLE B1 ---------------------------------------------------
# b1_title = sm.LabelWidget(master, 'Step 9: Locate Neck Position.', 1, 1, default_font, default_font_size, tk.W)