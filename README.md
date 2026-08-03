The Story: The Dangerous Dropshipper

You just got hired as the sole QA at a startup. The startup doesn't make its own products; they dropship.

Their website's backend automatically pulls products and prices from a third-party supplier's API: [https://fakestoreapi.com](https://fakestoreapi.com)

The Business Risk:
Last week, the supplier's database glitched. A $1,000 TV was suddenly listed with a price of $0.00. Your company's website automatically copied that data, and 50 people "bought" a free TV before the CEO noticed. The company lost $50,000 in an hour.

Your boss says: "I don't care how you do it, but write an automated script that checks the supplier's API every morning. If any product is priced at zero, negative, or is missing a title, I want the test to fail so our system shuts down before we lose more money."
