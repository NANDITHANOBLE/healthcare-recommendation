/**
 * Healthcare Recommender System
 * Client-side JavaScript for handling form submission and displaying results
 */

document.addEventListener('DOMContentLoaded', function() {
  // Get DOM elements
  const recommendForm = document.getElementById('recommendForm');
  const patientIdInput = document.getElementById('patientId');
  const symptomsInput = document.getElementById('symptoms');
  const resultsSection = document.getElementById('resultsSection');
  const resultsContent = document.getElementById('resultsContent');
  const errorMessage = document.getElementById('errorMessage');
  const loadingElement = document.getElementById('loading');
  
  // Form submission handler
  recommendForm.addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Hide any previous error messages and results
    errorMessage.style.display = 'none';
    resultsSection.classList.remove('active');
    
    // Show loading indicator
    loadingElement.style.display = 'block';
    
    // Get form values
    const patientId = patientIdInput.value.trim();
    const symptoms = symptomsInput.value.trim();
    
    // Client-side validation
    if (!patientId) {
      showError('Please enter a patient ID');
      return;
    }
    
    if (!symptoms) {
      showError('Please enter symptoms');
      return;
    }
    
    // Prepare data for API request
    const data = {
      patient_id: patientId,
      symptom_desc: symptoms
    };
    
    // Send API request
    fetch('/recommend', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => {
          throw new Error(err.error || 'Server error. Please try again.');
        });
      }
      return response.json();
    })
    .then(data => {
      // Hide loading indicator
      loadingElement.style.display = 'none';
      
      // Display results
      displayResults(data);
    })
    .catch(error => {
      // Hide loading indicator
      loadingElement.style.display = 'none';
      
      // Show error message
      showError(error.message);
    });
  });
  
  // Function to display error message
  function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    loadingElement.style.display = 'none';
  }
  
  // Function to display recommendation results
  function displayResults(data) {
    // Clear previous results
    resultsContent.innerHTML = '';
    
    // Add patient information section
    const patientInfo = data.patient_info;
    const patientInfoHTML = `
      <div class="patient-info">
        <h3 class="section-title">Patient Information</h3>
        <div class="patient-card">
          <div class="info-item">
            <span class="info-label">Patient ID:</span> ${patientInfo.id}
          </div>
          <div class="info-item">
            <span class="info-label">Age:</span> ${patientInfo.age}
          </div>
          <div class="info-item">
            <span class="info-label">Gender:</span> ${patientInfo.gender}
          </div>
          <div class="info-item">
            <span class="info-label">Current Conditions:</span>
            <div class="tag-list">
              ${patientInfo.conditions.map(condition => 
                `<span class="tag">${condition}</span>`).join('')}
            </div>
          </div>
          <div class="info-item">
            <span class="info-label">Current Treatments:</span>
            <div class="tag-list">
              ${patientInfo.current_treatments.map(treatment => 
                `<span class="tag">${treatment}</span>`).join('')}
            </div>
          </div>
        </div>
      </div>
    `;
    
    // Add similar patients section
    const similarPatientsHTML = `
      <div class="similar-patients">
        <h3 class="section-title">Similar Patients</h3>
        ${data.similar_patients.length > 0 ? 
          data.similar_patients.map(patient => `
            <div class="patient-card">
              <div class="info-item">
                <span class="info-label">Patient ID:</span> ${patient.id}
              </div>
              <div class="info-item">
                <span class="info-label">Age:</span> ${patient.age}
              </div>
              <div class="info-item">
                <span class="info-label">Gender:</span> ${patient.gender}
              </div>
              <div class="info-item">
                <span class="info-label">Conditions:</span>
                <div class="tag-list">
                  ${patient.conditions.map(condition => 
                    `<span class="tag">${condition}</span>`).join('')}
                </div>
              </div>
              <div class="info-item">
                <span class="info-label">Current Treatments:</span>
                <div class="tag-list">
                  ${patient.current_treatments.map(treatment => 
                    `<span class="tag">${treatment}</span>`).join('')}
                </div>
              </div>
            </div>
          `).join('') : 
          '<p>No similar patients found.</p>'
        }
      </div>
    `;
    
    // Add recommended treatments section
    const treatmentsHTML = `
      <div class="treatments">
        <h3 class="section-title">Recommended Treatments</h3>
        ${data.recommended_treatments.map(treatment => `
          <div class="treatment-card">
            <div class="treatment-name">${treatment[0]}</div>
            <div class="treatment-desc">${treatment[1]}</div>
          </div>
        `).join('')}
      </div>
    `;
    
    // Combine all sections
    resultsContent.innerHTML = patientInfoHTML + similarPatientsHTML + treatmentsHTML;
    
    // Show results section
    resultsSection.classList.add('active');
    
    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth' });
  }
});
