
# Password Algorithm 🔑
Generate many secure passwords by remembering only one phrase, one algorithm, and the number of breaches per account.

As this is a relatively complex way of generating, obtaining, and recovering a password, this is meant to be used by developers for their accounts, servers, etc. that need to be extremely secure. For example, the AWS root account, client web server, GitHub account, etc. passwords could be generated, obtained, and recovered using this algorithm.

## How it works
The algorithm takes in the following values:
- Website - Website you are logging in
- Username - Username for the website
- Secret - This is the string that will act as your "password for everything." This is the same for any account
- Breaches - The number of password breaches for this account.
- Security Level - A number which determines the length of your returned password

Afterwards, the algorithm will hash these values. That initial hash will be fed into another function - [pAlgorithm](https://github.com/thisLexic/palgorithm/blob/4709a85e3a159e5ecf35c3436ded1d09bdd42290/palgorithm.py#L54) - which will be uniquely defined by the developer. This function will return the final password for an account.


## Is it Secure?

The initial hash could be indexed, flipped, appended, rehashed, etc. in the pAlgorithm function before reaching the final password. This way, even if the secret were compromised, the attacker would still need to determine the developer's unique algorithm to get to the final password.

If the account password does get compromised, the password can easily be changed just for that account by incrementing the number of breaches for that one account. As this algorithm uses SHA512, there is an avalanche effect. One change - the breach count - should generate another completely different password.

Using SHA512, even if the password were compromised, the developer's inputs - the secret - should remain safe as this hash function cannot be reverse engineered (at the moment). Though even if it were possible, it would still be significantly difficult to do so as the [pAlgorithm](https://github.com/thisLexic/palgorithm/blob/4709a85e3a159e5ecf35c3436ded1d09bdd42290/palgorithm.py#L54) function is uniquely implemented by the developer.

## TLDR How to Use
1. Run [palgorithm.py](https://github.com/thisLexic/palgorithm/blob/main/palgorithm.py)
2. Enter your website, username, secret, breach count, and security on the CLI
3. Get your password

## Detailed How to Use
1. Copy [palgorithm.py](https://github.com/thisLexic/palgorithm/blob/main/palgorithm.py) (change [pAlgorithm](https://github.com/thisLexic/palgorithm/blob/4709a85e3a159e5ecf35c3436ded1d09bdd42290/palgorithm.py#L54) if necessary)
2. Run the script on the command line
3. Enter the website you will sign in (ex: aws, github, gmail)
4. Enter the username/email/id for the account (ex: hackerman, hack@sample.<span>com</span>, djangoUbuntu18AWSServer)
5. Enter your secret. 
6. Enter the number of password breaches for this account.
7. Enter the security level of the password.
8. Obtain your password

## Strengths
- You only need to remember 2 things (secret and algorithm) to generate all your passwords
- You don't have to rely on an external password manager for securing and remembering your passwords
- Isolates a password breach to only one account

## Limitations
- Certain websites have password restrictions (e.g. Use of special characters though this can be overcome by editing the [pAlgorithm](https://github.com/thisLexic/palgorithm/blob/4709a85e3a159e5ecf35c3436ded1d09bdd42290/palgorithm.py#L54) function)
- The secret may be compromised as it is typed for any password, regardless of security (e.g. secret is the same for a Facebook account and an AWS root account)
- The algorithm may be compromised if the file is compromised
- The number of breaches per account has to be stored externally (JSON, file, Database, etc.) as remembering this for each account is prone to forgetting
- A compromised secret or compromised algorithm entails creating a new one and, therefore, regenerating all your passwords for all your accounts
- Technically, you still have to remember the security level you used for an account. (However, since there ought to only be a few values for this, it shouldn't be a big hindrance.)

## Usage for Non-Coders
This algorithm requires a developer to define a unique sub-algorithm within it to work properly. For this reason, non-coders cannot use this as they cannot code their own unique sub-algorithm. 

However, it could be possible to create an algorithm which does not require a unique sub-algorithm to be defined by a developer. Perhaps two secrets can be used - the first one will be used in the initial hash and then the second one can be used in the secondary hash.

This should provide some security. However, it is not as secure as a unique sub-algorithm. 

This is only a possible solution and is not, at the moment, implemented in this repository.
