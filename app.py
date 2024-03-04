import streamlit as st

# Function to predict loan approval
def predict_loan_approval(applicant_data):
    # Preprocess user input similar to the training data
    applicant_data['Dependents'] = applicant_data['Dependents'].replace(to_replace='3+', value=4)
    applicant_data.replace({'Married': {'No': 0, 'Yes': 1}, 'Gender': {'Male': 1, 'Female': 0},
                            'Self_Employed': {'No': 0, 'Yes': 1},
                            'Property_Area': {'Rural': 0, 'Semiurban': 1, 'Urban': 2},
                            'Education': {'Graduate': 1, 'Not Graduate': 0}}, inplace=True)

    # Make prediction using the trained SVM model
    prediction = classifier.predict([applicant_data.values])

    return prediction[0]

# Streamlit UI
st.title("Loan Approval Prediction App")

# Get user input
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Marital Status", ["No", "Yes"])
dependents = st.slider("Number of Dependents", 0, 4, 0)
education = st.selectbox("Education", ["Not Graduate", "Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Create a dictionary with user input
user_input = {'Gender': gender, 'Married': married, 'Dependents': dependents,
              'Education': education, 'Self_Employed': self_employed, 'Property_Area': property_area}

# Convert user input into a DataFrame
user_data = pd.DataFrame([user_input])

# Make prediction
if st.button("Predict Loan Approval"):
    prediction = predict_loan_approval(user_data)
    st.write(f"The loan is {'Approved' if prediction == 1 else 'Not Approved'}")
