import random
import matplotlib.pyplot as plt
import pandas as pd

NUM_SIMULATIONS = 1000000

def main():
    sum_counts = { sum_val: 0 for sum_val in range(2, 13) }

    for _ in range(NUM_SIMULATIONS):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1

    # Calculate Monte Carlo probabilities
    monte_carlo_probs = { sum_val: count / NUM_SIMULATIONS for sum_val, count in sum_counts.items() }

    # Analytical probabilities from the image
    analytical_probs = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }

    sums = list(monte_carlo_probs.keys())
    monte_carlo_values = list(monte_carlo_probs.values())
    analytical_values = [analytical_probs[sum_val] for sum_val in sums]

    comparison_df = pd.DataFrame({
        'Sum': sums, 
        'Monte Carlo Probability': monte_carlo_values,
        'Analytical Probability': analytical_values
    })

    # Display the comparison table
    comparison_df['Monte Carlo Probability'] = comparison_df['Monte Carlo Probability'].apply(lambda x: f"{x:.2%}")
    comparison_df['Analytical Probability'] = comparison_df['Analytical Probability'].apply(lambda x: f"{x:.2%}")
    comparison_df = comparison_df.set_index('Sum')
    print(comparison_df)

    # Plotting the probabilities
    plt.figure(figsize=(10, 6))
    plt.bar(sums, monte_carlo_values, width=0.4, label='Monte Carlo', align='center')
    plt.bar([s + 0.4 for s in sums], analytical_values, width=0.4, label='Analytical', align='center')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Monte Carlo vs Analytical Probabilities for Sum of Two Dice')
    plt.legend()
    plt.xticks(sums)
    plt.show()

if __name__ == '__main__':
    main()