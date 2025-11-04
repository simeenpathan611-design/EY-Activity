few_shots = [
    #modelling Tables
    {   
        'Question': "Give the list of plants available?",
        'SQLQuery': "SELECT DISTINCT [Plant] FROM model_output_capacity_calculation",
        'SQLResult': "[('Facility6',), ('Facility5',), ('Facility4',), ('Facility2',), ('Facility1',), ('Facility3',)]",
        'Answer': "Facility6, Facility5, Facility4, Facility2, Facility1, Facility3'"
    },
    {
        'Question': "What is the scheduled quantity for a plant facility4?",
        'SQLQuery': "SELECT TOP 5 [Scheduled_Quantity] FROM model_output_allocation_details WHERE [Plant_Name] = 'Facility4'",
        'SQLResult': "[(275496.62999999995,), (130616.98,), (332930.96619999997,), (29882.2,), (758337.7756,)]",
        'Answer': "Scheduled quantity for Facility4 is 275496.6 or Two lakh and seventy five thousands."
    },
    
    {
        'Question': "What was the Attainment for every months?",
        'SQLQuery': "SELECT [Month], SUM(Scheduled_Quantity)/SUM(Allocated_Demand) AS Attainment FROM model_output_allocation_details GROUP BY [Month];",
        'SQLResult': "[(6, 0.52397304896282), (10, 0.5445719706848615), (2, 0.4510958816825768), (7, 0.4930497511680773), (9, 0.5572453367493116), (12, 0.44523298162863845), (4, 0.5260737853314852), (8, 0.5187475361431749), (3, 0.4393517595204879), (11, 0.5321914296538537), (5, 0.505231829594697), (1, 0.5054857947606384)] ",
        'Answer': "The Attainment for every month is listed in the SQLResult, with the month and the corresponding attainment value. (Jun, 0.52), (Oct, 0.54), (Feb, 0.45), (Jul, 0.49), (Sep, 0.55), (Dec, 0.44), (Apr, 0.52), (Aug, 0.51), (Mar, 0.43), (Nov, 0.53), (May, 0.50), (Jan, 0.50)"
    },
    {
        'Question': "What was the Attainment for the month of January?",
        'SQLQuery': "SELECT [Month], SUM(Scheduled_Quantity)/SUM(Allocated_Demand) AS Attainment FROM model_output_allocation_details GROUP BY [Month] having [Month] = 1;",
        'SQLResult': "[(1, 0.5054857947606384)] ",
        'Answer': "The Attainment for the month Jan is 0.52"
    },
    {
        'Question': "What is the scheduled quantity for a plant facility2 in the month of May?",
        'SQLQuery': "SELECT TOP 5 [Scheduled_Quantity] FROM model_output_allocation_details WHERE [Plant_Name] = 'Facility2' AND [Month] = 5",
        'SQLResult': "[(24119.46,), (78067.06,), (57019.37,), (575676.3193,), (21160.59,)]",
        'Answer': "The scheduled quantity for a plant facility2 in the month of May is 24119.46."
    },
    {
        'Question': "Give all the processing line that are available?",
        'SQLQuery': "SELECT DISTINCT [Processing_Line] FROM model_output_capacity_calculation",
        'SQLResult': "[('PL 16',), ('PL 7',), ('PL 18',), ('PL 15',), ('PL 6',), ('PL 19',), ('PL 20',), ('PL 17',), ('PL 11',), ('PL 12',), ('PL 14',), ('PL 22',), ('PL 2',), ('PL 8',), ('PL 21',), ('PL 23',), ('PL 10',), ('PL 3',), ('PL 4',), ('PL 9',), ('PL 13',), ('PL 1',)] ",
        'Answer': "All the available processing lines are PL 16, PL 7, PL 18, PL 15, PL 6, PL 19, PL 20, PL 17, PL 11, PL 12, PL 14, PL 22, PL 2, PL 8, PL 21, PL 23, PL 10, PL 3, PL 4, PL 9, PL 13, PL 1."
    },
    {
        'Question': "What is the utilization percentage of a processing line PL 6?",
        'SQLQuery': "SELECT TOP 1 [Plant], [Processing_Line], [Processing_Line_Days_Allocation], [Scheduled_Quantity], [Processing_Capacity_in_Available_Days], [Total_Capacity] FROM model_output_yearly_capacity_left WHERE [Processing_Line] = 'PL 6' ORDER BY [Processing_Line_Days_Allocation] DESC",
        'SQLResult': "[('Facility6', 'PL 6', 47.78, 5469325.069599999, 3962089.2410974586, 9431414.310697459)]",
        'Answer': "The utilization percentage of processing line PL 6 is 47.78%."
    },
    {
        'Question': "Provide all the products that are available?",
        'SQLQuery': "SELECT DISTINCT [Food] FROM model_output_allocation_details",
        'SQLResult': "[(' Caramel Crush Frosties ',), (' Chocolate Chip Nuggets ',), (' Vanilla Velvet Tidbits ',), (' Frosted Figs Wholemeal',), (' Malted Multigrain Mornings',), (' Crazy Coconut Nuggets ',), (' Strawberry Delight Nuggets ',), (' Strawberry Surprise Crunchies ',), (' Cranberry Crunch Multigrain',), (' Brownie Bite Wholemeal ',), (' Coconut Crumble Tidbits ',), (' Fruit Sugar Spheres   ',), (' Honey Harmony Tidbits ',), (' Pecan Pie Flakes ',), (' Marshmallow Sugar Stars ',), (' Oatmeal Golden Nuggets ',), (' Almond Dream Tidbits ',), (' Chocolate Chip Tidbits',), (' Cinnamon Puff Pops ',), (' Banana Bite Crunch   ',), (' Frosted Frappe Multigrain',), (' Winter Wheat Flakes ',), (' Chocolate Cherish Crunchies ',), (' Honey Bear Puffs ',), (' Cinnamon Celebration Squarez ',), (' Tangy Tart Wholemeal',), (' Creamy Cashew Wholemeal ',), (' Fruity Feast Tidbits ',), (' Berry Blast Frosties ',), (' Caramel Candy Tidbits ',), (' Choco Sugar Balls  ',), (' Vanilla Sugar Sparkles ',), (' Caramel Candy Crunchies ',), (' Minty Magic Squarez ',), (' Nutty Nugget Crunch ',), (' Whole Wheat nuggets',), (' Vanilla Vogue Wholemeal ',), (' Blueberry Bliss Squarez ',), (' Cocoa Cloud Puffs ',), (' Chocolate Craze Crispies ',), (' Sunrise Crunch  ',), (' Caramel Corn Crunch  ',), (' Coconut Cream Crunchies ',), (' Vanilla Vortex Crunchies ',), (' Harvest Honey Multigrain',), (' Chocolate Cluster Crunch ',), (' Malted Milk Nuggets ',), (' Tropical Tidbit Puffs',), (' Spicy Caramel Crispies ',), (' Banana Blend Multigrain',), (' Marshmallow Magic Crispies ',), (' Buttered Popcorn Crunchies ',), (' Cinnamon Circa Multigrain ',), (' Honey Heaven Squarez ',), (' Honey Sugar Wheels   ',), (' Lemon Luscious Crunchies ',), (' Maple Mingle Flakes ',), (' Pearlescent Puff Pearls',), (' Barely Blended Flakes ',), (' Lemon Lush Frosties ',), (' Nutty Nugget Squarez ',), (' Sugar Sprinkled Puffs ',), (' Tropical Treat Crispies ',), (' Munchy Mulberry Puffs',), (' Orange Overload Squarez ',), (' Nutella Nudge Crispies ',), (' Sweet Syrup Crunch ',), (' Frosted Sugar Flakes ',), (' Fruity Flake Fiesta',), (' Milky Malt Frosties ',), (' Corny Crispies ',), (' Forest Fruit Nuggets ',), (' Vanilla Velvet Nuggets ',), (' Banana Bliss Tidbits ',), (' Blueberry Bundle Crispies ',), (' Fresh Fruit Wholemeal',), (' Vanilla Vivacity Frosties ',), (' Vanilla Velvet Multigrain ',), (' Caramel Cloud Squarez ',), (' Chocolate Choice Wholemeal',), (' Biscuit Bliss Crunchies ',), (' Tropical Sugar Puffs  ',), (' Tangy Tart Flakes ',), (' Blueberry Bliss Nuggets ',), (' Spicy Cinnamon Flakes ',), (' Strawberry Splash Frosties ',), (' Chocolate Chunk Frosties ',), (' Green Apple Crispies ',), (' Caramel Corn Multigrain ',), (' Tropical Tango Frosties ',), (' Berry Blast Crunch ',), (' Vanilla Delight Crunch   ',)]",
        'Answer': "All the products that are available are listed below. Caramel Crush Frosties, Chocolate Chip Nuggets, Vanilla Velvet Tidbits, Frosted Figs Wholemeal,  Malted Multigrain Mornings,  Crazy Coconut Nuggets, Strawberry Delight Nuggets, Strawberry Surprise Crunchies, Cranberry Crunch Multigrain,  Brownie Bite Wholemeal, Coconut Crumble Tidbits, Fruit Sugar Spheres  , Honey Harmony Tidbits, Pecan Pie Flakes, Marshmallow Sugar Stars, Oatmeal Golden Nuggets, Almond Dream Tidbits, Chocolate Chip Tidbits,  Cinnamon Puff Pops, Banana Bite Crunch  , Frosted Frappe Multigrain,  Winter Wheat Flakes, Chocolate Cherish Crunchies, Honey Bear Puffs, Cinnamon Celebration Squarez, Tangy Tart Wholemeal,  Creamy Cashew Wholemeal, Fruity Feast Tidbits, Berry Blast Frosties, Caramel Candy Tidbits, Choco Sugar Balls , Vanilla Sugar Sparkles, Caramel Candy Crunchies, Minty Magic Squarez, Nutty Nugget Crunch, Whole Wheat nuggets,  Vanilla Vogue Wholemeal, Blueberry Bliss Squarez, Cocoa Cloud Puffs, Chocolate Craze Crispies, Sunrise Crunch , Caramel Corn Crunch , Coconut Cream Crunchies, Vanilla Vortex Crunchies, Harvest Honey Multigrain,  Chocolate Cluster Crunch, Malted Milk Nuggets, Tropical Tidbit Puffs,  Spicy Caramel Crispies, Banana Blend Multigrain,  Marshmallow Magic Crispies, Buttered Popcorn Crunchies, Cinnamon Circa Multigrain, Honey Heaven Squarez, Honey Sugar Wheels  , Lemon Luscious Crunchies, Maple Mingle Flakes, Pearlescent Puff Pearls,  Barely Blended Flakes, Lemon Lush Frosties, Nutty Nugget Squarez, Sugar Sprinkled Puffs, Tropical Treat Crispies, Munchy Mulberry Puffs,  Orange Overload Squarez, Nutella Nudge Crispies, Sweet Syrup Crunch, Frosted Sugar Flakes, Fruity Flake Fiesta,  Milky Malt Frosties, Corny Crispies, Forest Fruit Nuggets, Vanilla Velvet Nuggets, Banana Bliss Tidbits, Blueberry Bundle Crispies, Fresh Fruit Wholemeal,  Vanilla Vivacity Frosties, Vanilla Velvet Multigrain, Caramel Cloud Squarez, Chocolate Choice Wholemeal,  Biscuit Bliss Crunchies, Tropical Sugar Puffs , Tangy Tart Flakes, Blueberry Bliss Nuggets, Spicy Cinnamon Flakes, Strawberry Splash Frosties, Chocolate Chunk Frosties, Green Apple Crispies, Caramel Corn Multigrain, Tropical Tango Frosties, Berry Blast Crunch, Vanilla Delight Crunch "
    },
    {
        'Question': "Which plant has the highest excess capacity?",
        'SQLQuery': "SELECT TOP 1 [Plant], [Total_Capacity] - [Scheduled_Quantity] AS excess_capacity FROM model_output_yearly_capacity_left ORDER BY excess_capacity DESC;",
        'SQLResult': "[('Facility2', 17763696.93253413)]",
        'Answer': "Facility2 is the plant has the highest excess capacity"
    },
    {
        'Question': "What is the total capacity of a processing line?",
        'SQLQuery': "SELECT SUM([Total_Capacity]) AS [Total Capacity] FROM model_output_yearly_capacity_left",
        'SQLResult': "[(1080763959.4176354,)]",
        'Answer': "The total capacity of a processing line is 1080763959.7 " 
    },
    {
        'Question': "How many plants are included in the schedule?",
        'SQLQuery': "SELECT COUNT(DISTINCT Plant_Name) AS count_plant FROM model_output_schedule_plant_demand",
        'SQLResult': "[(6,)]",
        'Answer': "There are 6 plants included in the schedule."
    },
    {
        'Question': "What is the total demand transferred to a new plant?",
        'SQLQuery': "SELECT SUM(Demand) AS Total_Demand_Transferred FROM model_output_demand_transfer WHERE shifted_flag = 1",
        'SQLResult': "[(259519158.8027041,)]",
        'Answer': "The total demand transferred to a new plant is 259519158.8"
    },
    {
        'Question': "What is the total packed quantity for a plant Facility5 in Feb month?",
        'SQLQuery': "SELECT SUM([Scheduled_Quantity]) AS 'Total Packed Quantity' FROM model_output_allocation_details ERE [Plant_Name] = 'Facility5' AND [Month] = 2",
        'SQLResult': "[(3370939.4631,)]",
        'Answer': "The total packed quantity for a plant Facility5 in Feb month is 3370939.4 units or Three million units "
    },
    {
        'Question': "Which plant has the highest total capacity?",
        'SQLQuery': "SELECT TOP 1 [Plant], [Total_Capacity] FROM model_output_yearly_capacity_left ORDER BY [Total_Capacity] DESC",
        'SQLResult': "[('Facility3', 42327911.85395436)]",
        'Answer': "Facility3 is the plant has the highest total capacity"
    },
    {'Question': "What is the total demand for a specific SKU description?",
     'SQLQuery': "SELECT SUM(Demand) AS Total_Demand FROM model_output_demand_transfer WHERE SKU_Description = 'Prod Desc 31'",
     'SQLResult': "[(3257486.8081879998,)]",
     'Answer': "The total demand for SKU description Prod Desc 31 is 3257486.8 or Three millions"
     },
    {
        'Question': "How many plants have excess capacity?",
        'SQLQuery': "SELECT COUNT(*) AS [Number of Plants with Excess Capacity] FROM model_output_yearly_capacity_left WHERE Processing_Capacity_in_Available_Days > Scheduled_Quantity",
        'SQLResult': "[(17,)]",
        'Answer': "17 plants have excess capacity."
    },
    {
        'Question': "provide all the packing type?",
        'SQLQuery': "SELECT DISTINCT [Packing_Type] FROM model_output_result",
        'SQLResult': "[('Pack 2',), ('Pack 7',), ('Pack 11',), ('Pack 12',), ('Pack 4',), ('Pack 5',), ('Pack 8',), ('Pack 13',), ('Pack 1',), ('Pack 6',), ('Pack 10',), ('Pack 9',)]",
        'Answer': "Pack 2, Pack 7, Pack 11, Pack 12, Pack 4, Pack 5, Pack 8, Pack 13, Pack 1, Pack 6, Pack 10, Pack 9"
    },
    {
        'Question': "What is the total demand for a packing type Pack 8?",
        'SQLQuery': "SELECT SUM(Demand) AS Total_Demand FROM model_output_demand_transfer WHERE Packing_Type = 'Pack 8'",
        'SQLResult': "[(139779367.55707002,)]",
        'Answer': "The total demand for a packing type Pack 8 is 139779367.5 units or 1.3 billions"
    },
    {'Question': "Which processing line has the highest shortfall in demand?",
     'SQLQuery': "SELECT TOP 1 [Processing_Line], [Shortfall] FROM model_output_capacity_calculation ORDER BY [Shortfall] DESC;",
     'SQLResult': "[('PL 18', 14238247.709921002)]",
     'Answer': "PL 18 is the processing line has the highest shortfall in demand"
     },
    {
        'Question': "How many days are allocated for processing a product Oatmeal Golden Nuggets?",
        'SQLQuery': "SELECT TOP 5 [Processing_Line_Days_Allocation] FROM model_output_yearly_capacity_left WHERE [Food] = 'Oatmeal Golden Nuggets';",
        'SQLResult': "5.0",
        'Answer': "5days are allocated for processing a product Oatmeal Golden Nuggets"
    },
    {
        'Question': "Total how many SKUs available in database?",
        'SQLQuery': "SELECT COUNT(DISTINCT SKU) AS 'Total SKUs' FROM model_output_demand_transfer",
        'SQLResult': "[(332,)]",
        'Answer': "In total 332 SKUs available in database"
    },
    {
        'Question': "What is the difference in demand between SKU 110000109 and SKU 110000198?",
        'SQLQuery': "SELECT [SKU], SUM([Demand]) AS Total_Demand FROM model_output_demand_transfer WHERE [SKU] IN (110000109, 110000198) GROUP BY [SKU];",
        'SQLResult': "[(110000109, 855198.144404), (110000198, 11496550.038219001)]",
        'Answer': "The difference in demand between SKU 110000109 and SKU 110000198 is 10641351.8 or 10millions"
    },
    {
        'Question': "Compare the total capacity left between processing lines PL 6 and PL 19",
        'SQLQuery': " SELECT [Processing_Line], SUM([Total_Capacity]) AS 'Total Capacity Left FROM model_output_yearly_capacity_left WHERE [Processing_Line] IN ('PL 6', 'PL 19') GROUP BY [Processing_Line] ",
        'SQLResult': "[('PL 6', 32100990.919446655), ('PL 19', 68690251.25396551)]",
        'Answer': "The total capacity left for processing line PL 6 is 32,100,990.92 and for processing line PL 19 is 68,690,251.25. Therefore, processing line PL 19 has more total capacity left."
    },
    {
        'Question': "provide all the processing lines available in database",
        'SQLQuery': "SELECT DISTINCT [Processing_Line] FROM model_output_allocation_details ",
        'SQLResult': "[('PL 16',), ('PL 7',), ('PL 18',), ('PL 15',), ('PL 6',), ('PL 19',), ('PL 17',), ('PL 14',), ('PL 12',), ('PL 11',), ('PL 20',), ('PL 2',), ('PL 8',), ('PL 22',), ('PL 21',), ('PL 23',), ('PL 10',), ('PL 4',), ('PL 3',), ('PL 13',), ('PL 1',), ('PL 9',)] ",
        'Answer': "PL 16, PL 7, PL 18, PL 15, PL 6, PL 19, PL 17, PL 14, PL 12, PL 11, PL 20, PL 2, PL 8, PL 22, PL 21, PL 23, PL 10, PL 4, PL 3, PL 13, PL 1, PL 9"
    },
    {
        'Question': "Which month shows the highest demand compared to the previous month?",
        'SQLQuery': "SELECT TOP 1 [Month], MAX([Demand]) AS Highest_Demand FROM model_output_schedule_plant_demand GROUP BY [Month] ORDER BY [Month] DESC ",
        'SQLResult': "[(12, 3993344.0)]",
        'Answer': "The month with the highest demand compared to the previous month is December (Month 12)."
    },
    {
        'Question': "Compare the packing line utilization between the plants Facility5 and Facility4",
        'SQLQuery': "SELECT TOP 5 [Month], [Packing_Line], [availabile_days], [Plant], [Packing_Line_Days_Allocated], [packing_line_utlisation] FROM model_output_packing_line_utlisation WHERE [Plant] = 'Facility5' OR [Plant] = 'Facility4' ORDER BY [Plant], [Month] ",
        'SQLResult': "[(1, 'L401', 23.5, 'Facility4', 0.38, 0.016170212765957447), (1, 'L403', 23.5, 'Facility4', 12.290000000000001, 0.5229787234042553), (1, 'L404', 23.5, 'Facility4', 3.31, 0.14085106382978724), (1, 'L405', 23.5, 'Facility4', 8.95, 0.38085106382978723), (1, 'L402', 23.5, 'Facility4', 11.899999999999999, 0.5063829787234042)] ",
        'Answer': "The packing line utilization for Facility5 and Facility4 are not directly comparable as they have different packing lines. However, based on the results of the query, it can be seen that Facility4 has a higher packing line utilization compared to Facility5 for the month of 1."
    },
    {
        'Question': "What is the difference in demand transfer between the plants Facility1 and Facility4?",
        'SQLQuery': "SELECT SUM(Demand) AS demand_transfer_difference FROM model_output_demand_transfer WHERE [Scheduled_Plant] = 'Facility1' AND [Demand_plant] = 'Facility4",
        'SQLResult': "[(814883.085012,)]",
        'Answer': "The difference in demand transfer between Facility1 and Facility4 is 814883.0 or Eight lakh units"
    },
    {
        'Question': "What is the total packed quantity between the months Jan, Feb, Mar.",
        'SQLQuery': "SELECT SUM(Scheduled_Quantity) AS Total_Packed_Quantity FROM model_output_allocation_details WHERE [Month] IN (1,2,3)",
        'SQLResult': "[(187568805.34189996,)]",
        'Answer': "The total packed quantity between the months Jan, Feb, Mar is 187568805.3 or 1.8 billions "
    },
    {
        'Question': "What was the number of available days of packaging?",
        'SQLQuery': "SELECT TOP 5 [availabile_days] FROM model_output_packing_line_utlisation ORDER BY [availabile_days] DESC",
        'SQLResult': "[(31.0,), (31.0,), (31.0,), (31.0,), (31.0,)]",
        'Answer': "The number of available days of packaging is 31 days"
    },
    {
        'Question': "Which month we had the highest throughput?",
        'SQLQuery': "SELECT TOP 1 [Month], SUM([Scheduled_Quantity]) AS Total_Throughput FROM model_output_allocation_details GROUP BY [Month] ORDER BY Total_Throughput DESC",
        'SQLResult': "[(6, 75169568.55359998)]",
        'Answer': "The month with the highest throughput was June (Month 6)."
    },
    #Manufacturing Tables
    {
        'Question': "List all facilities available for Manufacturer 1",
        'SQLQuery': "SELECT [ManufacturerFacilityId] FROM dim_manufacturerfacilitybuilding WHERE [ManufacturerId] = 1",
        'SQLResult': "[('Facility1',), ('Facility2',), ('Facility3',), ('Facility4',), ('Facility5',), ('Facility6',)]",
        'Answer': "Facility1, Facility2, Facility3, Facility4, Facility5, Facility6"
    },

    {
        'Question': "Which manufacturing facility is available for most number of days?",
        'SQLQuery': "SELECT TOP 1 [ManufacturerFacilityId], SUM([Available_Days]) AS [Total_Available_Days] FROM dim_manufacturerfacilitylinecal GROUP BY [ManufacturerFacilityId] ORDER BY [Total_Available_Days] DESC",
        'SQLResult': "[('Facility3', Decimal('15673.50000000'))]",
        'Answer': "The manufacturing facility available for the most number of days is Facility3 with a total of 15673 days."
    },
    {
        'Question': "what are the start and end dates for the line with highest availablity for manufacturing facility 6?",
        'SQLQuery': "SELECT TOP 1 [ManufacturerFacilityBuildingCalendarStart], [ManufacturerFacilityBuildingCalendarEnd] FROM dim_manufacturerfacilitylinecal WHERE [ManufacturerFacilityId] = 'Facility6' AND [Available_Days] = (SELECT MAX([Available_Days]) FROM dim_manufacturerfacilitylinecal WHERE [ManufacturerFacilityId] = 'Facility6')",
        'SQLResult': "[(datetime.date(2023, 6, 1), datetime.date(2023, 6, 30))]",
        'Answer': "The start and end dates for the line with the highest availability for manufacturing facility 6 are June 1, 2023 and June 30, 2023."
    },

    {
        'Question': "which line has the highest availablity among all months? provide the building and facility id as well.",
        'SQLQuery': "SELECT TOP 1 [LineId], [BuildingId], [ManufacturerFacilityId], SUM([Available_Days]) AS [Total_Available_Days] FROM dim_manufacturerfacilitylinecal GROUP BY [LineId], [BuildingId], [ManufacturerFacilityId] ORDER BY [Total_Available_Days] DESC",
        'SQLResult': "[(12, 'B1', 'Facility2', Decimal('592.00000000'))]",
        'Answer': "The line with the highest availability among all months is Line 12 in Building B1 at Facility2 with a total of 592 available days."
    },

    {
        'Question': "which line has the highest availablity between 5th Feb and end before 18th August?",
        'SQLQuery': "SELECT TOP 1 [LineId], SUM([Available_Days]) AS [Total_Available_Days] FROM dim_manufacturerfacilitylinecal WHERE [ManufacturerFacilityBuildingCalendarStart] >= '2023-02-05' AND [ManufacturerFacilityBuildingCalendarEnd] < '2023-08-18' GROUP BY [LineId] ORDER BY [Total_Available_Days] DESC",
        'SQLResult': "[(150, Decimal('251.00000000'))]",
        'Answer': "The line with the highest availability between February 5, 2023 and August 18, 2023 is 150"
    },

    {
        'Question': "What is the timeline for master schedule MS1?",
        'SQLQuery': "SELECT [MasterSchedulePeriodStartDate], [MasterSchedulePeriodEndDate] FROM dim_masterschedule WHERE [MasterScheduleId] = 'MS1'",
        'SQLResult': "[(datetime.date(2023, 1, 1), datetime.date(2023, 1, 31))]",
        'Answer': "The timeline for master schedule MS1 is from January 1, 2023 to January 31, 2023."
    },

    {
        'Question': "List all master schedules that start after 5th Feb and end before 18th August. ",
        'SQLQuery': "SELECT [MasterScheduleId] FROM dim_masterschedule WHERE [MasterSchedulePeriodStartDate] > '2023-02-05' AND [MasterSchedulePeriodEndDate] < '2023-08-18'",
        'SQLResult': "[('MS3',), ('MS4',), ('MS5',), ('MS6',), ('MS7',)]",
        'Answer': "MS3, MS4, MS5, MS6, MS7"
    },

    {
        'Question': "for Activity A9819, how much extra quantity of units were produced? ",
        'SQLQuery': "SELECT ([ActualRunUnitQuantity] - [PlannedRunUnitQuantity]) AS [Extra Quantity Produced] FROM fact_manufacturing WHERE [ActivityId] = 'A9819'",
        'SQLResult': "[(Decimal('4061.79'),)]",
        'Answer': "4061.79 units were produced in excess."
    },

    {
        'Question': "List all run ids where 50 percent more units were actually produced compared to original planned units",
        'SQLQuery': "SELECT RunId FROM fact_manufacturing WHERE [ActualRunUnitQuantity] > ([PlannedRunUnitQuantity] * 1.5)",
        'SQLResult': "[('Run2174',), ('Run2837',), ('Run3495',), ('Run4153',), ('Run2154',), ('Run3470',), ('Run2828',), ('Run3486',), ('Run4140',), ('Run4144',), ('Run3461',), ('Run2785',), ('Run2800',), ('Run3443',), ('Run3458',), ('Run4116',), ('Run2807',), ('Run3464',), ('Run4122',), ('Run4780',), ('Run2179',), ('Run2832',), ('Run3490',), ('Run4148',), ('Run4806',), ('Run4811',), ('Run2166',), ('Run2170',), ('Run2824',), ('Run3482',), ('Run4798',), ('Run4802',), ('Run2812',), ('Run4128',), ('Run4786',), ('Run2127',), ('Run2142',), ('Run4101',), ('Run4759',), ('Run4774',), ('Run2145',), ('Run2803',), ('Run4119',), ('Run4777',), ('Run2149',), ('Run3465',), ('Run4123',), ('Run4781',), ('Run2148',), ('Run2806',)]",
        'Answer': "50% more units were actually produced in the following run ids: Run2174, Run2837, Run3495, Run4153, Run2154, Run3470, Run2828, Run3486, Run4140, Run4144, Run3461, Run2785, Run2800, Run3443, Run3458, Run4116, Run2807, Run3464, Run4122, Run4780, Run2179, Run2832, Run3490, Run4148, Run4806, Run4811, Run2166, Run2170, Run2824, Run3482, Run4798, Run4802, Run2812, Run4128, Run4786, Run2127, Run2142, Run4101, Run4759, Run4774, Run2145, Run2803, Run4119, Run4777, Run2149, Run3465, Run4123, Run4781, Run2148, Run2806."
    },

    {
        'Question': "what are the facilities that produced 20000 units more than planned units during runs between Feb and August?",
        'SQLQuery': "SELECT DISTINCT[ManufacturerFacilityId] FROM fact_manufacturing WHERE [ActualRunUnitQuantity] - [PlannedRunUnitQuantity] > 20000 AND [ActivityStartTimestamp] BETWEEN '2023-02-01' AND '2023-08-31' ORDER BY [ManufacturerFacilityId]",
        'SQLResult': "[('Facility2',), ('Facility3',), ('Facility4',), ('Facility5',)]",
        'Answer': "20000 more units were actually produced in the following facilities between February 5, 2023 and August 18, 2023: Facility2, Facility3, Facility4, Facility5"
    },
    
    { 
        'Question': "what are the facilities that produced 20000 units more than planned units during runs between Feb and August?. Dont repeat names",
        'SQLQuery': "SELECT DISTINCT [ManufacturerFacilityId] FROM fact_manufacturing WHERE [PlannedRunUnitQuantity] - [ActualRunUnitQuantity] > 20000 AND [ActivityStartTimestamp] BETWEEN '2023-02-01' AND '2023-08-31'",
        'SQLResult': "[('Facility5',), ('Facility4',), ('Facility6',), ('Facility2',), ('Facility1',), ('Facility3',)]",
        'Answer': "The facilities that produced 20000 units more than planned units during runs between February 5, 2023 and August 18, 2023 are Facility5, Facility4, Facility6, Facility2, Facility1, and Facility3."
    },
    
    { 
        'Question': "Which line produced the most quantity of items for all runs combined?",
        'SQLQuery': "SELECT TOP 1 [LineId], SUM([ActualRunUnitQuantity]) AS 'Total Quantity' FROM fact_manufacturing GROUP BY [LineId] ORDER BY [Total Quantity] DESC",
        'SQLResult': "[(97, Decimal('61868220.49'))]",
        'Answer': "97 line produced the most quantity of items for all runs combined with total quantity of 61868220.49"
    },
    
    { 
        'Question': "which manufacturing facility produces the most quantity of items over and above the original planned quantity? Ignore negative quantities or where production is zero",
        'SQLQuery': "SELECT TOP 1 [ManufacturerFacilityId], SUM([ActualRunUnitQuantity] - [PlannedRunUnitQuantity]) AS excess_quantity FROM fact_manufacturing WHERE [ActualRunUnitQuantity] > 0 AND [PlannedRunUnitQuantity] > 0 GROUP BY [ManufacturerFacilityId] ORDER BY excess_quantity DESC;",
        'SQLResult': "[('Facility1', Decimal('3786069.67'))]",
        'Answer': "Facility1"
    },
    
    { 
        'Question': "what are the average quantity values produced top 3 leading build plan?",
        'SQLQuery': "SELECT TOP 3 AVG([PlannedRunUnitQuantity]) FROM fact_manufacturing GROUP BY [BuildPlanId] ORDER BY AVG([PlannedRunUnitQuantity]) DESC",
        'SQLResult': "[(Decimal('3993344.120000'),), (Decimal('3157424.890000'),), (Decimal('2460740.210000'),)]",
        'Answer': "Three leading build plans have an average quantity of 3,993,344.12, 3,157,424.89, and 2,460,740.21."
    },
    
    { 
        'Question': "How many Manufacturer Facilites are available?",
        'SQLQuery': "SELECT COUNT(DISTINCT [ManufacturerFacilityId]) FROM dim_manufacturerfacility",
        'SQLResult': "[(6,)]",
        'Answer': "There are 6 Manufacturer Facilities available."
    },
    
    { 
        'Question': "What are top five Manufacturer Facilites having highest production quantity?",
        'SQLQuery': "SELECT TOP 5 [ManufacturerFacilityId], SUM([ActualRunUnitQuantity]) AS 'Total Production Quantity' FROM fact_manufacturing GROUP BY [ManufacturerFacilityId] ORDER BY [Total Production Quantity] DESC",
        'SQLResult': "[('Facility3', Decimal('1169018882.82')), ('Facility6', Decimal('795826731.86')), ('Facility4', Decimal('643355633.84')), ('Facility1', Decimal('501332970.20')), ('Facility2', Decimal('477033482.00'))]",
        'Answer': "Five Manufacturer Facilities with the highest production quantity are Facility3, Facility6, Facility4, Facility1, and Facility2."
    },
    
    { 
        'Question': "How many build plans fall within a specific date range from 01-06-2023 till 30-06-2023?",
        'SQLQuery': "SELECT COUNT(*) FROM dim_buildplan WHERE [BuildPlanPeriodStartDate] >= '2023-06-01' AND [BuildPlanPeriodEndDate] <= '2023-06-30'",
        'SQLResult': "[(5771,)]",
        'Answer': "5771 build plans fall within the date range from 01-06-2023 till 30-06-2023."
    },
    
    { 
        'Question': "Which build plans have a higher actual production quantity than planned?",
        'SQLQuery': "SELECT TOP 10 [BuildPlanId], [ActualProductionQuantity], [PlannedRunUnitQuantity] FROM fact_manufacturing WHERE [ActualProductionQuantity] > [PlannedRunUnitQuantity] ORDER BY [ActualProductionQuantity] DESC;",
        'SQLResult': "[('BP319', 'ActualProductionQuantity', 608000.0), ('BP478', 'ActualProductionQuantity', 421275.0), ('BP786', 'ActualProductionQuantity', 295750.0), ('BP853', 'ActualProductionQuantity', 273000.0), ('BP947', 'ActualProductionQuantity', 247500.0)]",
        'Answer': "Build plans BP319, BP478, BP786, BP853, and BP947 have a higher actual production quantity than planned."
    },
    
    { 
        'Question': "Which build plans were created most recently?",
        'SQLQuery': "SELECT TOP 10 [BuildPlanName] FROM dim_buildplan ORDER BY [BuildPlanCreatedDate] DESC",
        'SQLResult': "[('BuildPlan449',), ('BuildPlan279',), ('BuildPlan411',), ('BuildPlan594',), ('BuildPlan1959',), ('BuildPlan2446',), ('BuildPlan3263',), ('BuildPlan2361',), ('BuildPlan30',), ('BuildPlan410',)]",
        'Answer': "BuildPlan449, BuildPlan279, BuildPlan411, BuildPlan594, BuildPlan1959, BuildPlan2446, BuildPlan3263, BuildPlan2361, BuildPlan30, BuildPlan410"
    },
    
    { 
        'Question': "How many build plans are set to start in the next month?",
        'SQLQuery': "SELECT COUNT(*) FROM dim_buildplan WHERE [BuildPlanPeriodStartDate] >= GETDATE() AND [BuildPlanPeriodStartDate] <= DATEADD(month, 1, GETDATE())",
        'SQLResult': "[(249,)]",
        'Answer': "249 build plans are set to start in the next month."
    },
    
    {    
        'Question': "How many items belong to the item category Crispies Clan?",
        'SQLQuery': "SELECT COUNT(*) AS [Number of Items in Creamy Crunchies Category] FROM dim_item WHERE [ItemCategory] LIKE '%Crispies Clan%'",
        'SQLResult': "[(92,)]",
        'Answer': "Total 92 items belong to the item category Crispies Clan."
    },
    
    { 
        'Question': "List all items with a weight greater than 10000 cubes",
        'SQLQuery': "SELECT TOP 10 [ItemSku], [ItemName], [ItemCategory], [ItemDescription], [ItemWeight] FROM dim_item WHERE [ItemWeight] > 10000 ORDER BY [ItemWeight] DESC",
        'SQLResult': "[(110000129, ' Sugar Sergents      ', ' Crispies Clan   ', 'Prod Desc 57', Decimal('33600.00')), (110000115, ' Tasty Tidbits   ', ' Crispies Clan   ', 'Prod Desc 244', Decimal('33600.00')), (110000109, ' Multigrain Mornings ', ' Flakes Family   ', 'Prod Desc 1', Decimal('23200.00')), (110000440, ' Tasty Tidbits   ', ' Wholesome Wholemeal ', 'Prod Desc 336', Decimal('22400.00')), (110000125, ' Puffs Family    ', ' Crispies Clan   ', 'Prod Desc 94', Decimal('20800.00')), (110000122, ' Puffs Family    ', ' Crispies Clan   ', 'Prod Desc 95', Decimal('19200.00')), (110000111, ' Sugar Sergents       ', ' Flakes Family   ', 'Prod Desc 23', Decimal('15360.00')), (110000134, ' Tasty Tidbits   ', ' Crispies Clan   ', 'Prod Desc 48', Decimal('14400.00')), (110000121, ' Tasty Tidbits   ', ' Crispies Clan   ', 'Prod Desc 50', Decimal('14400.00')), (110000106, ' Creamy Crunchies ', ' Puffs Family    ', 'Prod Desc 161', Decimal('14240.00'))]",
        'Answer': "There are 10 items with a weight greater than 10000 cubes: Sugar Sergents, Tasty Tidbits, Multigrain Mornings, Tasty Tidbits, Puffs Family, Puffs Family, Sugar Sergents, Tasty Tidbits, Tasty Tidbits, and Creamy Crunchies."
    },
    
    { 
        'Question': "Tabulate the list of additive and its unique item counts belong to the additive catagory",
        'SQLQuery': "SELECT [Additives], COUNT(DISTINCT [ItemSku]) AS Unique_Item_Count FROM dim_item GROUP BY [Additives]",
        'SQLResult': "[(None, 6), ('Single', 26), ('Dual', 2), ('No Additives', 308)]",
        'Answer': "The list of additives and their corresponding unique item counts are listed in the SQLResult. There are 6 items with no additives, 26 items with single additives, 2 items with dual additives, and 308 items with no additives listed."
    },
    
    { 
        'Question': "Which item forecasts were created most recently?",
        'SQLQuery': "SELECT TOP 10 [ItemSku], [ItemCustomerDemandForecastStartDate] FROM dim_itemcustomerdemandforecast ORDER BY [ItemCustomerDemandForecastStartDate] DESC",
        'SQLResult': "[(110000208, datetime.date(2024, 12, 1)), (110000103, datetime.date(2024, 12, 1)), (110000170, datetime.date(2024, 12, 1)), (110000128, datetime.date(2024, 12, 1)), (110000110, datetime.date(2024, 12, 1)), (110000199, datetime.date(2024, 12, 1)), (110000198, datetime.date(2024, 12, 1)), (110000203, datetime.date(2024, 12, 1)), (110000209, datetime.date(2024, 12, 1)), (110000117, datetime.date(2024, 12, 1))]",
        'Answer': "The item forecasts created most recently are for the following items: 110000208, 110000103, 110000170, 110000128, 110000110, 110000199, 110000198, 110000203, 110000209, 110000117."
    },
    
    { 
        'Question': "What is the average packing speed of lines in facility 3?",
        'SQLQuery': "SELECT AVG([PackingSpeed]) FROM dim_line WHERE [ManufacturerFacilityId] = 'Facility3'",
        'SQLResult': "[(Decimal('102.6000000'),)]",
        'Answer': "The average packing speed of lines in facility 3 is 102.60"
    },
    
    { 
        'Question': "Which Manufacturer Facility were most recently installed?",
        'SQLQuery': "SELECT TOP 1 [ManufacturerFacilityId], [BuildPlanCreatedDate] FROM dim_buildplan ORDER BY [BuildPlanCreatedDate] DESC ",
        'SQLResult': "[('Facility3', datetime.date(2024, 1, 1))]",
        'Answer': "Facility3 was most recently installed on 2024-01-01."
    },
    
    { 
        'Question': "How many facilities are there in the US West region?",
        'SQLQuery': "SELECT COUNT(*) FROM dim_manufacturerfacility WHERE [Location] = 'US West'",
        'SQLResult': "[(2,)]",
        'Answer': "Two facilities are located in the US West region."
    },
    
    { 
        'Question': "List all facilities with their latitude and longitude coordinates.",
        'SQLQuery': "SELECT [ManufacturerFacilityId], [Latitude], [Longitude] FROM dim_manufacturerfacility",
        'SQLResult': "[('Facility1', Decimal('31.1696'), Decimal('-99.6836')), ('Facility2', Decimal('44.3148'), Decimal('-85.6024')), ('Facility3', Decimal('37.2296'), Decimal('-120.0475')), ('Facility4', Decimal('27.6648'), Decimal('-81.5158')), ('Facility5', Decimal('34.1685'), Decimal('-111.6681')), ('Facility6', Decimal('40.4173'), Decimal('-82.9071'))]",
        'Answer': "Facility1: Latitude: 31.1696, Longitude: -99.6836, Facility2: Latitude: 44.3148, Longitude: -85.6024, Facility3: Latitude: 37.2296, Longitude: -120.0475,Facility4: Latitude: 27.6648, Longitude: -81.5158, Facility5: Latitude: 34.1685, Longitude: -111.6681, Facility6: Latitude: 40.4173, Longitude: -82.9071"
    }

]
