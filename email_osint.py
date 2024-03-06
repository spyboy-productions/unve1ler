import re
import dns.resolver
import requests
from bs4 import BeautifulSoup

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

# Replace with the target email address you want to investigate
#target_email = "xyz@gmail.com" #input("Email:")


# Function to extract the domain from an email address
def extract_domain(email):
    match = re.search(r'@(.+)', email)
    if match:
        return match.group(1)
    return None


# Function to fetch MX (Mail Exchanger) records for a domain
def get_mx_records(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return [mx.exchange.to_text() for mx in mx_records]
    except dns.resolver.NXDOMAIN:
        return []
    except dns.exception.Timeout:
        return []
    except Exception as e:
        print(f"{R}An error occurred while fetching MX records: {str(e)}")
        return []


# Function to perform a Google search and return the search results
def perform_google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an exception if the request fails

        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all("h3")
    except requests.exceptions.RequestException as e:
        print(f"{R}An error occurred while performing the Google search: {str(e)}")
        return []


# Function to extract all links from the given HTML string.
def extract_links(html):
    """Extracts all links from the given HTML string.

    Args:
      html: A string containing HTML code.

    Returns:
      A list of all links extracted from the HTML string.
    """

    links = re.findall(r'href="([^"]*)"', html)
    return links


# Function to fetch and print more information from a website
def fetch_and_print_info(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            if text:
                print(f"    Additional Info: {text}")
    except Exception as e:
        print(f"{R}Error while fetching more info from {url}: {str(e)}")


# Function to crawl a website
def crawl_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract all links from the website
    links = [link['href'] for link in soup.find_all('a')]

    # Crawl all of the links
    for link in links:
        crawl_website(link)


# Function to perform extensive OSINT on the email address using Google dorks
def osint_with_google_dorks(email, domain):
    google_dorks = [
        f'site:linkedin.com/in {email}',
        f'site:facebook.com {email}',
        f'site:instagram.com {email}',
        f'site:twitter.com {email}',
        f'site:github.com {email}',
        f'site:stackoverflow.com {email}',
        f'site:medium.com {email}',
        f'site:quora.com {email}',
        f'site:gitlab.com {email}',
        f'site:bitbucket.org {email}',
        f'site:soundcloud.com {email}',
        f'site:youtube.com {email}',
        f'site:vimeo.com {email}',
        f'site:twitch.tv {email}',
        f'site:discord.gg {email}',
        f'site:paypal.me {email}',
        f'site:venmo.com {email}',
        f'site:reddit.com/r/{email}',
        f'site:pastebin.com/u/{email}',
        f'site:archive.org/web/*/{email}',
        f'site:whois.com/{domain} AND "email: {email}"',
        f'"email: {email}" AND "filetype:pdf"',
        f'site:arxiv.org/search/?q=all:{email}&submit=Search',
    ]

    '''
    f'site:linkedin.com/in {email} AND "software engineer"',
    f'site:github.com {email} AND "python"',
    f'site:twitter.com {email} AND "machine learning"',
    f'site:github.com {email} AND "stars:>100"',
    f'site:twitter.com {email} AND "followers:>1000"',
    f'site:linkedin.com/in {email} AND "connections:>500"',
    f'site:medium.com {email} AND "published:>10"',
    f'site:stackoverflow.com {email} AND "reputation:>1000"',
    f'site:quora.com {email} AND "answers:>100"',
    '''

    if google_dorks:
        print(f"\n{C}[+] {Y}Social media Google dorks search results for {C}{email}:{W}\n")
        for dork in google_dorks:
            search_results = perform_google_search(f'"{dork}"')
            if search_results:
                for result in search_results:
                    result_text = result.get_text()
                    result_links = extract_links(str(result))
                    if result_links:
                        try:
                            result_link = result_links[0]
                            print(f"{G}- {result_text}")
                            print(f"{C}Link:{Y} {result_link}")
                        except TypeError:
                            print(f"{W}Not able to fetch the link, Google it.")
                    else:
                        print(f"{G}- {result_text}")
                        print(f"{W}Not able to fetch the link, Google it.")
            else:
                print(f"{R}No results found for {W}{dork}.")
    else:
        print(f"{R}No Google dorks specified for {Y}{email}.")

# Function to perform extensive OSINT on the email address using Google dorks
def osint_with_google_dorks2(email):
    query = f'"{email}"'
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("h3")

        if search_results:
            print(f"\n{C}[+] {Y}Google dorks search results for {C}{email}:{W}\n")
            for result in search_results:
                result_text = result.get_text()
                result_links = extract_links(str(result))
                if result_links:
                    try:
                        result_link = result_links[0]
                        print(f"{G}- {result_text}")
                        print(f"{C}Link:{Y} {result_link}")
                    except TypeError:
                        print(f"{W}Not able to fetch the link, Google it.")
                else:
                    print(f"{G}- {result_text}")
                    print(f"{W}Not able to fetch the link, Google it.")

        else:
            print(f"No Google dorks results found for {email}.")
    else:
        print(f"{R}An error occurred while performing the Google dorks search.")

if __name__ == "__main__":
    domain = extract_domain(target_email)
    if domain:
        print(f"\n{C}[+] {Y}Email Domain:{G} {domain}")
        mx_records = get_mx_records(domain)
        if mx_records:
            print(f"\n{C} [+]{Y}Mail Exchanger (MX) Records:{G}")
            for mx in mx_records:
                print(f"  - {mx}")
        else:
            print(f"{R}No MX records found for the domain.")
    else:
        print(f"{R}Invalid email address format.")

    # Perform extensive OSINT on the email address using Google dorks
    osint_with_google_dorks(target_email)
    osint_with_google_dorks2(target_email)


