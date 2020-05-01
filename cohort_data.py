"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code

    active_file = open(filename)
    houses = set([line.rstrip().split("|")[2] for line in active_file 
             if line.rstrip().split("|")[2] != ""])

    """
    houses = set()

    for line in active_file:

      data = line.rstrip().split("|")
      house = data[2]

      if house != "":
        houses.add(house)
    """

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    # TODO: replace this with your code
    active_file = open(filename)

    for line in active_file:
      data = line.rstrip().split("|")
      first, last, _, _, students_cohort = data
      name = first + " " + last

      if cohort == 'All' and students_cohort not in {"I", "G"}:
        students.append(name)

      elif students_cohort == cohort:
        students.append(name)

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code
    active_file = open(filename)

    for line in active_file:
      data = line.rstrip().split("|")  #[first, last, house, adviser, cohort]
      name = data[0] + " " + data[1]
      house = data[2]
      cohort = data[4]

      if house == "Dumbledore's Army":
        dumbledores_army.append(name)
      elif house == "Gryffindor":
        gryffindor.append(name)
      elif house == "Hufflepuff":
        hufflepuff.append(name)
      elif house == "Ravenclaw":
        ravenclaw.append(name)
      elif house == "Slytherin":
        slytherin.append(name)
      elif cohort == "G":
        ghosts.append(name)
      else:
        instructors.append(name)

    rosters = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, 
              slytherin, ghosts, instructors]
    
    for roster in rosters:
      roster.sort()
    
    return rosters


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code
    active_file = open(filename)

    for line in active_file:

      data = line.rstrip().split("|")    #[first, last, house, adviser, cohort]
      data[:2] = [data[0] + " " + data[1]]
      data = tuple(data)
      all_data.append(data)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code
    active_file = open(filename)

    for line in active_file:

      data = line.rstrip().split("|")
      students_name = data[0] + " " + data[1]
      cohort = data[4]

      if students_name == name:
        return cohort


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    duplicates = set()
    last_names = set()

    active_file = open(filename)

    for line in active_file:

      data = line.rstrip().split("|")
      last = data[1]

      if last in last_names:
        duplicates.add(last)

      else:
        last_names.add(last)

    return duplicates


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code
    data = all_data(filename)

    for student in data:
      if student[0] == name:
        house = student[1]
        cohort = student[3]
        break

    housemates = set()
    for student in data:
      student_name = student[0]
      students_house = student[1]
      students_cohort = student[3]
      if (students_house == house and students_cohort == cohort and 
          student_name != name):
        housemates.add(student_name)

    return housemates


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
