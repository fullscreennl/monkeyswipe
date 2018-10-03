import shutileasy_levels = ['A_Mazing','Eifel_Brought_Us_Tower','Part_Of_A_Chain','Easy_Peacy','Chevy_To_The_Levy','Ball_n_Chain','Tony_Hawk','The_Hitman','Easy_Does_It','The_Maze_You_Special','X_Games','Wired','Release_The_Cheese','Jump_Up_And_Get_Down','Anger_Management','Destroy_The_Dangler','Clockwork_Monkey','Blade_Walker','Friendly_Push','Huh_What_Now','Swing_A_Beam','Rag_Doll','Captain_Caveman','AI_Enemy','Rotor_Bombing','Twelve_Monkies','The_M_Lost_His_Mind','Dodge_It','Unfriendly_Family','Dropping_Bars','Grave_Digger','The_Swing','The_Dance','Kick_Out_The_Jams','Thunder_Struck','Bump','Wabi_Sabi','Boom_Town','Free_Willy']

medium_levels = ['Tumbling_Down','Spikey_On_A_Rail','Nice_Moustache','Wired_Again','They_Will_Get_You','Total_Workout','Chained_Reaction','Fly_Flies','Will_It_Blend','Bouncer','I_Can_See_Spikey','Tumble_Drop','Get_In_The_Car','Daily_Mahal','Bump_The_Chump','Fast_Eddy','The_Pitcher','Muchos_Nachos','Wip_Wap','Chain_Reaction','Just_Swing','Surfs_Up','Keep_Em_Save','Seen_Before','Were_Are_The_Boids','Chopper','What_The_Font','The_Follower','Robocod','The_Hardest_Button','Connected_To_Spikey','What_The_Bomb','Up_The_Shaft','Accelerate_Now','Jump_Ramp','Bombs_Ahead','Triple_Touch','Beat_The_Bugger','Dazzling_With_BS']

hard_levels = ['Another_Bombtrack','Monkey_Eat_Dust','Little_Buddha','The_Carrier','MonkeyFace','Domino_D_Day','Maze_Of_Doom','Our_House','One_Too_Many','Chop_Chop_Burito','Climb_Up','The_Bridge_Too_Far','Pinball_Madness','Mission_Impossible','Crowded_House','Cant_Move','Stay_Mellow','House_With_A_View','Hole_In_The_Floor','Its_A_Long_Way','It_Can_Be_Done','Monkey_in_Wonderland','Diabolic_Car','Keep_Em_Rolling','No_Escape','It_Dont_Mean_A_Thing','I_Can_Feel_Tension','Coming_From_Above','Come_And_Get_It','Strange_Rotors','Surf_Safari','Rise_Above','World_Tower_Fund','Multi_Ball','HimmelBau','Connected','Are_Those_pigs','Cant_Find_Spikey','Pentagram']

packs = [(easy_levels,'levels_2'), (medium_levels,'levels_3'), (hard_levels,'levels_4')]

#folders = ['levels_2','levels_3','levels_4']folders = ['dummy']bg_colors = ["blue","green","yellow","red","grey","purple"]

for p in packs:
	print p
	print "** "*20	counter = 0
	for l in p[0]:
		#print "looking for : "+l 
		for f in folders:
			try:				#shutil.copyfile(f+"/"+l+".py","organized_levels/"+p[1]+"/"+l+".py")				print "(\""+l+"\", 4,60,\""+bg_colors[counter%6]+"_bg.png\"),"				counter += 1
				raise "found"				#print "- - - - - - - - "
			except:
				pass 
		#print "- "*20
	
	
	
	
	
	
	
	
	