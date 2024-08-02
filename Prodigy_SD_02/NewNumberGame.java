// Imported necessary libraries for the game
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class NewNumberGame {
    private JFrame frame;
    private JLabel titleLabel;
    private JLabel label;
    private JLabel attemptsLabel;
    private JTextField textField;
    private JButton submitButton;
    private int targetNumber;
    private int attempts;
    private int maxAttempts;
    private int score;

    public NewNumberGame() {
        frame = new JFrame("Number Guessing Game - JK");
        frame.getContentPane().setBackground(new Color(255, 255, 255));

        titleLabel = new JLabel("Play the Number Guessing Game by JK in Java");
        titleLabel.setFont(new Font("Poppins", Font.BOLD, 24)); 
        titleLabel.setForeground(new Color(0, 0, 139)); 
        titleLabel.setHorizontalAlignment(JLabel.CENTER);

        label = new JLabel("Enter your guessed number between 1 & 100:");
        label.setFont(new Font("Poppins", Font.BOLD, 19));
        label.setHorizontalAlignment(JLabel.CENTER);

        attemptsLabel = new JLabel("Attempts: 0");
        attemptsLabel.setFont(new Font("Poppins", Font.BOLD, 19));
        attemptsLabel.setHorizontalAlignment(JLabel.CENTER);

        textField = new JTextField(10);
        textField.setColumns(10);
        textField.setBackground(new Color(255, 255, 255));
        textField.setFont(new Font("Poppins", Font.BOLD, 17));
        textField.setPreferredSize(new Dimension(120, 30));
        textField.setHorizontalAlignment(JTextField.CENTER);

        submitButton = new JButton("Submit");
        submitButton.setBackground(new Color(33, 142, 66));
        submitButton.setFont(new Font("Poppins", Font.BOLD, 17));
        submitButton.setForeground(Color.BLACK); 
        submitButton.setFocusPainted(true);
        submitButton.setPreferredSize(new Dimension(100, 30));
        submitButton.setHorizontalAlignment(JTextField.CENTER);

        targetNumber = generateRandomNumber();
        maxAttempts = 8;
        attempts = 0;
        score = 0;

        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                checkGuess();
            }
        });

        JPanel panel = new JPanel();
        panel.setLayout(new GridBagLayout());
        panel.setBackground(new Color(255, 255, 204));

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        gbc.weightx = 1;
        panel.add(titleLabel, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        gbc.weightx = 1;
        panel.add(label, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2;
        gbc.weightx = 1;
        panel.add(attemptsLabel, gbc);

        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 1;
        gbc.weightx = 1;
        gbc.fill = GridBagConstraints.NONE;
        gbc.anchor = GridBagConstraints.CENTER;
        panel.add(textField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.gridwidth = 1;
        gbc.weightx = 1;
        gbc.fill = GridBagConstraints.CENTER;
        gbc.anchor = GridBagConstraints.CENTER;
        panel.add(submitButton, gbc);

        frame.add(panel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(580, 290);
        frame.setLocationRelativeTo(null); 
        frame.setVisible(true);
        frame.setResizable(false);
    }

    private int generateRandomNumber() {
        Random random = new Random();
        return random.nextInt(100) + 1;
    }

    private void checkGuess() {
        int userGuess;
        try {
            userGuess = Integer.parseInt(textField.getText());
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(frame, "Please enter a valid number.");
            return;
        }
        attempts++;

        attemptsLabel.setText("Attempts: " + attempts);

        if (userGuess == targetNumber) {
            JOptionPane.showMessageDialog(frame, "Congratulations! You guessed the correct number.");
            score++;
        } else if (attempts < maxAttempts) {
            String message = (userGuess < targetNumber) ? "Too low! Try a higher number." : "Too high! Try a lower number.";
            JOptionPane.showMessageDialog(frame, message);
        } else {
            JOptionPane.showMessageDialog(frame, "Sorry! You've used all your attempts. The correct number was " + targetNumber);
        }

        if (attempts < maxAttempts) {
            targetNumber = generateRandomNumber();
            textField.setText("");
        } else {
            showScore();
        }
    }

    private void showScore() {
        JOptionPane.showMessageDialog(frame, "Your final score is: " + score);
        int option = JOptionPane.showConfirmDialog(frame, "Do you want to play again?", "Play Again", JOptionPane.YES_NO_OPTION);
        if (option == JOptionPane.YES_OPTION) {
            resetGame();
        } else {
            frame.dispose();
        }
    }

    private void resetGame() {
        targetNumber = generateRandomNumber();
        attempts = 0;
        attemptsLabel.setText("Attempts: 0");
        score = 0;
        textField.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new NewNumberGame();
            }
        });
    }
}
