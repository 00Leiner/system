from scheduler import Scheduler 

if __name__ == "__main__":
    rooms = [
        {
            'name': "room1",
            'availability': [
                {
                    'day': "Monday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Tuesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Wednesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Thursday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Friday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Sunday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                }
                # Add more availability
            ]
        },
        {
            'name': "room2",
            'availability': [
                {
                    'day': "Monday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Tuesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Wednesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Thursday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Friday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Sunday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                }
                # Add more availability
            ]
        },
        {
            'name': "room3",
            'availability': [
                {
                    'day': "Monday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Tuesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Wednesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Thursday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Friday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Sunday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                }
                # Add more availability
            ]
        },
        {
            'name': "room4",
            'availability': [
                {
                    'day': "Monday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Tuesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Wednesday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Thursday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Friday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                },
                {
                    'day': "Sunday",
                    'time': [ '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', 
                             '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', 
                             '13:00', '13:30', '14:00', '14:30','15:00', '15:30', 
                             '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', 
                             '19:00', '19:30', '20:00', '12:30' ],
                }
                # Add more availability
            ]
        },
        # Add more rooms
    ]

    teachers = [
        {
            'name': "teacher1",
            'preferredCourses': [
                {
                    'code': "IT 4102",
                    'description': "Mobile App Development",
                    'units': "3" 
                },
                {
                    'code': "IT 1101",
                    'description': "Information Technology Fundamentals",
                    'units': "3" 
                },
                {
                    'code': "CS 5204",
                    'description': "Data Mining",
                    'units': "3" 
                },
                # Add more courses
            ]
        },
        {
            'name': "teacher2",
            'preferredCourses': [
                {
                    'code': "CS 2107", 
                    'description': "Data Structures and Algorithm", 
                    'units': 3
                },
                {
                    'code': "IT 2105", 
                    'description': "System Analysis and Design", 
                    'units': 3
                },
                {
                    'code': "IT 2207", 
                    'description': "Web Development", 
                    'units': 3
                },
                    # Add more subjects here
            ]
        },
        {
            'name': "teacher3",
            'preferredCourses': [
                {
                    'code': "CS 2201",
                    'description': "Database Systems",
                    'units': "3" 
                },
                {
                    'code': "CS 3105",
                    'description': "Operating Systems",
                    'units': "3" 
                },
                {
                    'code': "CS 3203",
                    'description': "Software Engineering",
                    'units': "3" 
                },
                # Add more courses
            ]
        },
        {
            'name': "teacher4",
            'preferredCourses': [
                {
                    'code': "CS 4109",
                    'description': "Computer Networks",
                    'units': "3" 
                },
                {
                    'code': "CS 4207",
                    'description': "Artificial Intelligence",
                    'units': "3" 
                },
                {
                    'code': "CS 5102",
                    'description': "Web Development",
                    'units': "3" 
                },
                # Add more courses
            ]
        },
        {
            'name': "teacher5",
            'preferredCourses': [
                {
                    'code': "IT 1203",
                    'description': "Database Management Systems",
                    'units': "3" 
                },
                {
                    'code': "IT 3109",
                    'description': "Software Engineering",
                    'units': "3" 
                },
                {
                    'code': "IT 3201",
                    'description': "Computer Networks",
                    'units': "3" 
                },
                {
                    'code': "IT 4204",
                    'description': "Cloud Computing",
                    'units': "3" 
                },
                # Add more courses
            ]
        }
        # Add more teachers
    ]

    program_blocks = [
        {
            'program': "BSCS",
            'year': [
                {
                    'year': "1",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "CS 2107",
                            'description': "Data Structures and Algorithm",
                            'unit': "3",
                        },
                        {
                            'code': "CS 2201",
                            'description': "Database Systems",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "1",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "CS 2107",
                            'description': "Data Structures and Algorithm",
                            'unit': "3",
                        },
                        {
                            'code': "CS 2201",
                            'description': "Database Systems",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "1",
                    'blocks': "C",
                    'courses': [
                        {
                            'code': "CS 2107",
                            'description': "Data Structures and Algorithm",
                            'unit': "3",
                        },
                        {
                            'code': "CS 2201",
                            'description': "Database Systems",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "2",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "CS 3105",
                            'description': "Operating Systems",
                            'unit': "3",
                        },
                        {
                            'code': "CS 3203",
                            'description': "Software Engineering",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "2",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "CS 3105",
                            'description': "Operating Systems",
                            'unit': "3",
                        },
                        {
                            'code': "CS 3203",
                            'description': "Software Engineering",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "3",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "CS 4109",
                            'description': "Computer Networks",
                            'unit': "3",
                        },
                        {
                            'code': "CS 4207",
                            'description': "Artificial Intelligence",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "3",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "CS 4109",
                            'description': "Computer Networks",
                            'unit': "3",
                        },
                        {
                            'code': "CS 4207",
                            'description': "Artificial Intelligence",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "3",
                    'blocks': "C",
                    'courses': [
                        {
                            'code': "CS 4109",
                            'description': "Computer Networks",
                            'unit': "3",
                        },
                        {
                            'code': "CS 4207",
                            'description': "Artificial Intelligence",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "3",
                    'blocks': "D",
                    'courses': [
                        {
                            'code': "CS 4109",
                            'description': "Computer Networks",
                            'unit': "3",
                        },
                        {
                            'code': "CS 4207",
                            'description': "Artificial Intelligence",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "4",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "CS 5102",
                            'description': "Web Development",
                            'unit': "3",
                        },
                        {
                            'code': "CS 5204",
                            'description': "Data Mining",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "4",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "CS 5102",
                            'description': "Web Development",
                            'unit': "3",
                        },
                        {
                            'code': "CS 5204",
                            'description': "Data Mining",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                # Add more year
            ]
        },
        {
            'program': "BSIT",
            'year': [
                {
                    'year': "1",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "IT 1101",
                            'description': "Information Technology Fundamentals",
                            'unit': "3",
                        },
                        {
                            'code': "IT 1203",
                            'description': "Database Management Systems",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "1",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "IT 1101",
                            'description': "Information Technology Fundamentals",
                            'unit': "3",
                        },
                        {
                            'code': "IT 1203",
                            'description': "Database Management Systems",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "2",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "IT 2105",
                            'description': "System Analysis and Design",
                            'unit': "3",
                        },
                        {
                            'code': "IT 2207",
                            'description': "Web Development",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "2",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "IT 2105",
                            'description': "System Analysis and Design",
                            'unit': "3",
                        },
                        {
                            'code': "IT 2207",
                            'description': "Web Development",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "2",
                    'blocks': "C",
                    'courses': [
                        {
                            'code': "IT 2105",
                            'description': "System Analysis and Design",
                            'unit': "3",
                        },
                        {
                            'code': "IT 2207",
                            'description': "Web Development",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "2",
                    'blocks': "D",
                    'courses': [
                        {
                            'code': "IT 2105",
                            'description': "System Analysis and Design",
                            'unit': "3",
                        },
                        {
                            'code': "IT 2207",
                            'description': "Web Development",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "3",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "IT 3109",
                            'description': "Software Engineering",
                            'unit': "3",
                        },
                        {
                            'code': "IT 3201",
                            'description': "Computer Networks",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "3",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "IT 3109",
                            'description': "Software Engineering",
                            'unit': "3",
                        },
                        {
                            'code': "IT 3201",
                            'description': "Computer Networks",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "4",
                    'blocks': "A",
                    'courses': [
                        {
                            'code': "IT 4102",
                            'description': "Mobile App Development",
                            'unit': "3",
                        },
                        {
                            'code': "IT 4204",
                            'description': "Cloud Computing",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "4",
                    'blocks': "B",
                    'courses': [
                        {
                            'code': "IT 4102",
                            'description': "Mobile App Development",
                            'unit': "3",
                        },
                        {
                            'code': "IT 4204",
                            'description': "Cloud Computing",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                {
                    'year': "4",
                    'blocks': "C",
                    'courses': [
                        {
                            'code': "IT 4102",
                            'description': "Mobile App Development",
                            'unit': "3",
                        },
                        {
                            'code': "IT 4204",
                            'description': "Cloud Computing",
                            'unit': "3",
                        },
                        # Add more courses
                    ]
                },
                # Add more year
            ]
        }
        # Add more programs
    ]

    # scheduler = Scheduler(rooms, teachers, program_blocks)
    # scheduler.define_variables()
    # scheduler.define_domains()
    # scheduler.define_constraints()
    # scheduler.solve()

    Scheduler()

