# Password Algorithm 🔑
Generate many secure passwords by remembering only one phrase and one algorithm

## TLDR How to Use
1. Run [palgorithm.py](https://github.com/thisLexic/palgorithm/blob/main/palgorithm.py)
2. Enter your website, username, secret, and security on the CLI
3. Get your password

## Detailed How to Use
1. Copy [palgorithm.py](https://github.com/thisLexic/palgorithm/blob/main/palgorithm.py)
2. Run the script on the command line
3. Enter the website you will sign in (ex: facebook, github, gmail)
4. Enter the username/email/id for the account (ex: hackerman, hack@sample.<span>com</span>, djangoUbuntu18AWSServer)
5. Enter your secret. This is the string that will act as your "password for everything." This is the same for any account in any given website.
6. Enter the security level of the password. This determines the length of your returned password
7. Obtain your password

## Strengths
- You only need to remember 2 things (secret and algorithm) to generate all your passwords
- You don't have to rely on an external password manager for securing and remembering your passwords
- Isolates a password breach to only one account in one website

## Limitations
- Certain websites have password restrictions (e.g. Use of capitalised and uncapitalised letters)
- The secret may be compromised as it is typed for any password, regardless of security (e.g. secret is the same for a Facebook account and an AWS root account)
- The algorithm may be compromised if the file is compromised
- A compromised secret or compromised algorithm entails creating a new one and, therefore, regenerating all your passwords for all your accounts
- Technically, you still have to remember the security level you used for an account. (However, since there ought to only be a few values for this, it shouldn't be a big hindrance.)
