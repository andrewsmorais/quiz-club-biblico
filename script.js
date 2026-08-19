let currentStep = 1;
const totalSteps = 6;

// Initialize progress bar on load
window.onload = () => {
    updateProgressBar();
    updateBackButtonVisibility();
};

// Quando o usuário seleciona uma opção
function selectOption(btn) {
    // Remove a classe 'selected' de outras opções no mesmo passo
    const parent = btn.parentElement;
    const siblings = parent.querySelectorAll('.option-btn');
    siblings.forEach(b => b.classList.remove('selected'));
    
    // Adiciona a classe 'selected' no botão clicado
    btn.classList.add('selected');
    
    // Avança para o próximo passo após um leve delay para dar o feedback visual
    setTimeout(() => {
        nextStep();
    }, 350);
}

function nextStep() {
    // Hide current step
    const currentElement = document.getElementById(`step-${currentStep}`);
    if (currentElement) {
        currentElement.classList.remove('active');
    }
    
    currentStep++;
    
    if (currentStep <= totalSteps) {
        // Show next question
        const nextElement = document.getElementById(`step-${currentStep}`);
        if (nextElement) {
            nextElement.classList.add('active');
        }
        updateProgressBar();
    } else {
        // Show loading screen (Step 6)
        const loadingElement = document.getElementById('loading-screen');
        if (loadingElement) {
            loadingElement.classList.add('active');
        }
        updateProgressBar(100);
        
        // Wait 3 seconds, then show final result (Step 7)
        setTimeout(() => {
            if (loadingElement) loadingElement.classList.remove('active');
            
            const resultElement = document.getElementById('result-screen');
            if (resultElement) {
                resultElement.classList.add('active');
            }
        }, 3000);
    }
    updateBackButtonVisibility();
}

function prevStep() {
    if (currentStep > 1) {
        // Esconde a etapa atual
        const currentElement = document.getElementById(`step-${currentStep}`);
        if (currentElement) {
            currentElement.classList.remove('active');
        }
        
        currentStep--;
        
        // Mostra a etapa anterior
        const prevElement = document.getElementById(`step-${currentStep}`);
        if (prevElement) {
            prevElement.classList.add('active');
        }
        updateProgressBar();
        updateBackButtonVisibility();
    }
}

function updateProgressBar(overridePercentage) {
    const progressBar = document.getElementById('progress-bar');
    if (!progressBar) return;
    
    if (overridePercentage !== undefined) {
        progressBar.style.width = overridePercentage + '%';
    } else {
        // Calculate percentage
        const percentage = ((currentStep - 1) / totalSteps) * 100;
        progressBar.style.width = percentage + '%';
    }
}

function updateBackButtonVisibility() {
    const backBtn = document.getElementById('global-back-btn');
    if (!backBtn) return;
    
    // Mostra o botão apenas se for maior que 1 e menor ou igual a totalSteps
    if (currentStep > 1 && currentStep <= totalSteps) {
        backBtn.style.display = 'flex';
    } else {
        backBtn.style.display = 'none';
    }
}
