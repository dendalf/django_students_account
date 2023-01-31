

def format_list_students(students):
    # string = '<br>'.join(str(student) for student in students)
    string = '<table><thead><tr><th>First name</th><th>Last name</th><th>Email</th><th>Birthdate</th><th>Phone number</th></thead><tbody>'
    for st in students:
        string += f'<tr><td>{st.first_name} </td><td>{st.last_name} </td><td>{st.email} </td><td>{st.birthdate} </td><td>{st.phone_number} </td></tr>'
    string += '</tbody></table>'
    return string
