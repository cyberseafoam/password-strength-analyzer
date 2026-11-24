import streamlit as st

from password_analyzer import (calculate_score, get_rating, get_suggestions,
                               check_length, check_uppercase, check_lowercase,
                               check_number, check_special, check_common)


st.title('Password Strength Analyzer')
st.write('Check how strong your password is!')
st.write('Created for BYU CS111')
password = st.text_input('Enter a sample password:', type='password')
if password != '':
    score = calculate_score(password)
    rating = get_rating(score)
    suggestions = get_suggestions(password)
    st.subheader('Password Strength')
    st.progress(score)
    st.write('Score:', score, '/ 100')
    st.write('Rating:', rating)
    if rating == 'Strong':
        st.success('Strong password!')
    elif rating == 'Moderate':
        st.warning('Your password could be stronger.')
    else:
        st.error('Weak password!')
    st.subheader('Security Checklist')
    if check_length(password):
        st.write('✅ At least 12 characters')
    else:
        st.write('❌ At least 12 characters')
    if check_uppercase(password):
        st.write('✅ Uppercase letter')
    else:
        st.write('❌ Uppercase letter')
    if check_lowercase(password):
        st.write('✅ Lowercase letter')
    else:
        st.write('❌ Lowercase letter')
    if check_number(password):
        st.write('✅ Number')
    else:
        st.write('❌ Number')
    if check_special(password):
        st.write('✅ Special character')
    else:
        st.write('❌ Special character')
    if not check_common(password):
        st.write('✅ Not in the common password list')
    else:
        st.write('❌ Common password detected')
    st.subheader('Suggestions')
    if len(suggestions) == 0:
        st.success('All basic checks passed!')
    else:
        for suggestion in suggestions:
            st.write('-', suggestion)
    st.info(
        'This is a basic educational strength estimate, '
        'not a guarantee of password security.'
    )
else:
    st.info('Enter a made-up password to begin.')