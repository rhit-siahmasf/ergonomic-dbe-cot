
# # Step B6 -----------------------------------------------------------------------------------------------
# # -------------------- OPTIONS B6 --------------------------------------------------
# b6_step_options = [sm.CheckButtonWidget(master, option_type, 'If load < 4.4 lbs (intermittent): (+0)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If load 4.4 to 22 lbs (intermittent): (+1)', 1, 1, tk.S),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If load 4.4 to 22 lbs (static or repeated): (+2)', 2, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If more than 22lbs OR repeated or shocks: (+3)', 2, 1, tk.S)]
# b6_title = sm.LabelWidget(master, 'Step 14: Add Force / Load Score', 1, 1, default_font, default_font_size, tk.W)
# b6_step_screen = sm.ScreenManager(master, b_trunk_title, b6_title, [], b6_step_options, all_others, None, None)
