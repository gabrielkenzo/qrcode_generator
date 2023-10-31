# QR Code Generator
I came across this concept in a Biology class that I took, where the professor gave us printed qrcodes that had small letters to each side of it. We used it to answer multiple choice questions.

He presented us questions with 4 alternatives, and we had to rotate our qrcode so that the alternative that we though was correct would be the letter in the upper side of the qrcode. He than scanned all qrcodes using his smartphone camera. Each qrcode was unique, so every one of us had a different one, with a number to represent us, that was shown in the screen along our answer. The qrcodes were 5x5 grids and I saw a pattern in them: every one had the same configuration in the internal 3x3 grid. This whole class had me wondering how many qrcodes it is possible to generate following these conditions:

- every rotation of each qrcode should be different than the other 3 rotations (so that we can differentiate the answers)
- every qrcode should be unique, considering its rotations

I spent a little time trying to get a mathmatical solution, a formula that gave me the answer to my question, but I failed (I'm kinda rusty in probabilistcs). So than I decided to compute it with the help of programming.

## QR Codes examples

![image](https://github.com/gabrielkenzo/qrcode_generator/assets/59087233/9de00538-6b00-44ac-8f44-e663f19b3d0b)
