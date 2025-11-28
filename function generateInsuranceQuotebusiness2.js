// Function to generate a business insurance quote
function generateInsuranceQuote(businessType, coverageAmount) {
    const baseRates = {
        'retail': 0.02,
        'construction': 0.03,
        'technology': 0.015,
        'healthcare': 0.025
    };

    const rate = baseRates[businessType.toLowerCase()] || 0.01; // Default rate
    const quote = coverageAmount * rate;

    return {
        businessType: businessType,
        coverageAmount: coverageAmount,
        quote: quote.toFixed(2)
    };
}

// Frontend function to handle form submission
document.getElementById('insuranceForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const businessType = document.getElementById('businessType').value;
    const coverageAmount = parseFloat(document.getElementById('coverageAmount').value);

    const quote = generateInsuranceQuote(businessType, coverageAmount);
    
    document.getElementById('quoteResult').innerText = `Your insurance quote for ${quote.businessType} is $${quote.quote}`;
});