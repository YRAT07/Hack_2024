from crewai import Task
from textwrap import dedent
from datetime import date

class TripTasks:

    def file_reader_task(self, agent, inputFile: str, logFile: str, computationCode: str):
        return Task(
            description=dedent(f"""
                You should read following files:
                1. inputFile, which is a json file containing input data. Path: {inputFile}
                2. logFile, which contains logs about code flow execution. Path: {logFile}
                3. computationCode, which contains python code. This code execution generates logs from input file. Path: {computationCode}

                Return the data in separate sections. For e.g.,
                Input file: <input file content>
                Log file: <log file content>
                Python file: <computation file content>
            """),
            agent=agent,
            expected_output="File contents for all 3 files, separated"
        )
    
    # def file_analyzer_task(self, agent):
    #     return Task(
    #         description=dedent(f"""
    #             You will be provided with 3 files contents appended as a single content.
    #             It will be a combination of 
    #         """)
    #     )

    # def gather_task(self, agent, origin, interests, range):
    #     return Task(
    #         description=dedent(f"""
    #             As a local expert on this city you must compile an 
    #             in-depth guide for someone traveling there and wanting 
    #             to have THE BEST trip ever!
    #             Gather information about key attractions, local customs,
    #             special events, and daily activity recommendations.
    #             Find the best spots to go to, the kind of place only a
    #             local would know.
    #             This guide should provide a thorough overview of what 
    #             the city has to offer, including hidden gems, cultural
    #             hotspots, must-visit landmarks, weather forecasts, and
    #             high level costs.
                
    #             The final answer must be a comprehensive city guide, 
    #             rich in cultural insights and practical tips, 
    #             tailored to enhance the travel experience.
    #             {self.__tip_section()}

    #             Trip Date: {range}
    #             Traveling from: {origin}
    #             Traveler Interests: {interests}
    #         """),
    #         agent=agent,
    #         expected_output="Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips"
    #     )

    # def plan_task(self, agent, origin, interests, range):
    #     return Task(
    #         description=dedent(f"""
    #             Expand this guide into a full 7-day travel 
    #             itinerary with detailed per-day plans, including 
    #             weather forecasts, places to eat, packing suggestions, 
    #             and a budget breakdown.
                
    #             You MUST suggest actual places to visit, actual hotels 
    #             to stay and actual restaurants to go to.
                
    #             This itinerary should cover all aspects of the trip, 
    #             from arrival to departure, integrating the city guide
    #             information with practical travel logistics.
                
    #             Your final answer MUST be a complete expanded travel plan,
    #             formatted as markdown, encompassing a daily schedule,
    #             anticipated weather conditions, recommended clothing and
    #             items to pack, and a detailed budget, ensuring THE BEST
    #             TRIP EVER. Be specific and give it a reason why you picked
    #             each place, what makes them special! {self.__tip_section()}

    #             Trip Date: {range}
    #             Traveling from: {origin}
    #             Traveler Interests: {interests}
    #         """),
    #         agent=agent,
    #         expected_output="Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown"
    #     )

    # def __tip_section(self):
    #     return "If you do your BEST WORK, I'll tip you $100!"
        
    #     """