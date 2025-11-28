function generateInsuranceQuote(businessName, businessType, coverageAmount) {
    const baseRate = 0.02; // Example base rate
    const coverageMultiplier = 1.5; // Example multiplier based on business type
    const quote = coverageAmount * baseRate * coverageMultiplier;

    return {
        businessName: businessName,
        businessType: businessType,
        coverageAmount: coverageAmount,
        quote: quote.toFixed(2)
    };
}

// Example usage
const quote = generateInsuranceQuote("Tech Solutions", "IT Services", 100000);
console.log(quote);