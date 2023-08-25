#!/usr/bin/env python3
# unve1ler: Revealing Digital Footprints and Visual Clues on the Internet
# A social engineering tool designed to seamlessly locate profiles using usernames while offering convenient reverse image search functionality.

import requests
import threading
import time
from datetime import datetime

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/unve1ler'


VERSION = '1.0.1'

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

current_date = datetime.now().date()
formatted_date = current_date.strftime("%Y-%m-%d")
TIMEOUT_SECONDS = 10

banner = r'''                                                    
                         ____.__                
 __ __  _______  __ ____/_   |  |   ___________ 
|  |  \/    \  \/ // __ \|   |  | _/ __ \_  __ \
|  |  /   |  \   /\  ___/|   |  |_\  ___/|  | \/
|____/|___|  /\_/  \___  >___|____/\___  >__|   
           \/          \/              \/
        Revealing Digital Footprints and Visual Clues on the Internet.       
                                                
'''


def print_banners():
    """
    prints the program banners
    """
    print(f'{R}{banner}{W}\n')
    print(f'{G}[+] {Y}Version      : {W}{VERSION}')
    print(f'{G}[+] {Y}Created By   : {W}Spyboy')
    print(f'{G} ╰➤ {Y}Twitter      : {W}{twitter_url}')
    print(f'{G} ╰➤ {Y}Discord      : {W}{discord}')
    print(f'{G} ╰➤ {Y}Website      : {W}{website}')
    print(f'{G} ╰➤ {Y}Blog         : {W}{blog}')
    print(f'{G} ╰➤ {Y}Github       : {W}{github}\n')


def check_platform(username, platform, url, results):
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)

        if response.status_code == 200:
            print(f"{G}Profile found on {Y}{platform}: {url}")
            results[platform] = url
        else:
            print(f"{R}Profile not found on {W}{platform}")
            results[platform] = None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking {platform}: {e}")
        results[platform] = None


def check_social_media(username, image_link=None):
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}/",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "inktr": f"https://linktr.ee/{username}",
        "GitHub": f"https://github.com/{username}",
        "Gitlab": f"https://gitlab.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "YouTube": f"https://www.youtube.com/user/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Vimeo": f"https://vimeo.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}/",
        "Dribbble": f"https://dribbble.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://{username}.deviantart.com",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Mix": f"https://mix.com/{username}",
        "Meetup": f"https://www.meetup.com/members/{username}",
        "Goodreads": f"https://www.goodreads.com/user/show/{username}",
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Viber": f"https://chats.viber.com/{username}",
        "Slack": f"https://{username}.slack.com",
        "Xing": f"https://www.xing.com/profile/{username}",
        "Canva": f"https://www.canva.com/{username}",
        "500px": f"https://500px.com/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "Foursquare": f"https://foursquare.com/user/{username}",
        "Kik": f"https://kik.me/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Periscope": f"https://www.pscp.tv/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Steemit": f"https://steemit.com/@{username}",
        "Vine": f"https://vine.co/u/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Zillow": f"https://www.zillow.com/profile/{username}",
        "TripAdvisor": f"https://www.tripadvisor.com/members/{username}",
        "Crunchyroll": f"https://www.crunchyroll.com/user/{username}",
        "Trello": f"https://trello.com/{username}",
        "Vero": f"https://www.vero.co/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "About.me": f"https://about.me/{username}",
        "Trakt": f"https://www.trakt.tv/users/{username}",
        "Couchsurfing": f"https://www.couchsurfing.com/people/{username}",
        "Craigslist": f"https://accounts.craigslist.org/login/home",
        "Behance": f"https://www.behance.net/{username}",
        "Etsy": f"https://www.etsy.com/shop/{username}",
        "Ebay": f"https://www.ebay.com/usr/{username}",
        "Bandcamp": f"https://bandcamp.com/{username}",
        "AngelList": f"https://angel.co/u/{username}",
        "Ello": f"https://ello.co/{username}",
        "Gravatar": f"https://en.gravatar.com/{username}",
        "Instructables": f"https://www.instructables.com/member/{username}",
        "VSCO": f"https://vsco.co/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}",
        "Houzz": f"https://www.houzz.com/user/{username}",
        "Digg": f"https://digg.com/@{username}",
        "Giphy": f"https://giphy.com/{username}",
        "Anchor": f"https://anchor.fm/{username}",
        "Scribd": f"https://www.scribd.com/{username}",
        "Grubhub": f"https://www.grubhub.com/profile/{username}",
        "ReverbNation": f"https://www.reverbnation.com/{username}",
        "Squarespace": f"https://{username}.squarespace.com",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "IMDb": f"https://www.imdb.com/user/ur{username}",
        "LinkBio": f"https://lnk.bio/{username}",
        "Relpit": f"https://replit.com/{username}",
        "Ifttt": f"https://ifttt.com/p/{username}",
        "Weebly": f"https://{username}.weebly.com/",
        "Smule": f"https://www.smule.com/{username}",
        "Wordpress": f"https://{username}.wordpress.com/",
        "Tryhackme": f"https://tryhackme.com/p/{username}",
        "Pateron": f"https://www.patreon.com/{username}",
        "Myspace": f"https://myspace.com/{username}",
        "Freelancer": f"https://www.freelancer.com/u/{username}",
        "Dev.to": f"https://dev.to/{username}",
        "Blogspot": f"https://{username}.blogspot.com",
        "Gist": f"https://gist.github.com/{username}",
        "Viki": f"https://www.viki.com/users/{username}/about",
        # ...
    }

    threads = []
    results = {}

    start_time = time.time()

    for platform, url in platforms.items():
        thread = threading.Thread(target=check_platform, args=(username, platform, url, results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    found_count = sum(1 for value in results.values() if value is not None)
    timeouts = sum(1 for value in results.values() if value is None and value is not False)
    errors = sum(1 for value in results.values() if value is False)

    print("-------------------------------------------------------\n")
    print(f"{C}[+] {R}Target: {W}{username}")
    print(f"{C}[+] {R}Looked through: {W}{len(platforms)} websites")
    print(f"{C}[+] {R}Time taken: {W}{elapsed_time:.2f} seconds")
    print(f"{C}[+] {R}Date: {W}{formatted_date}")
    print(f"{C}[+] {R}Profiles found: {W}{found_count}")
    print(f"{C}[-] {R}Timeouts: {W}{timeouts}")
    print(f"{C}[-] {R}Errors: {W}{errors}\n")
    print(f"{C}[+] {Y}Found URLs ({R}Note: there can be false positive links):\n")
    for platform, url in results.items():
        if url:
            print(f"{Y}{platform}: {G}{url}")

    if image_link:
        print(f'\n{W}[+] {C}Reverse Image Search URLs:\n')
        print(f"{G}Google: {Y}https://lens.google.com/uploadbyurl?url={image_link}\n"
              f"{G}Bing: {Y}https://www.bing.com/images/search?view=detailv2&iss=sbi&form=SBIVSP&sbisrc=UrlPaste&q=imgurl:{image_link}\n"
              f"{G}Yandex: {Y}https://yandex.com/images/search?source=collections&&url={image_link}&rpt=imageview\n"
              f"{G}Baidu: {Y}https://graph.baidu.com/details?isfromtusoupc=1&tn=pc&carousel=0&image={image_link}")

    print("-------------------------------------------------------")


def main():
    print_banners()
    target_username = input(f'{C}Target Username: ')

    if not target_username:
        print(f"{R}Error: Target username not provided.{W}")
        return

    response = input(f"{Y}Do you have any image of the target? (yes/no): ").lower()

    if response == "yes":
        image_link = input(f"{G}Great! Type/paste the image link: ")

        try:
            response = requests.get(image_link, timeout=5)

            if response.status_code == 200:
                print(f'{W}Reverse image URL will be printed in the end.')

            else:
                print("Invalid image link.")

        except Exception as e:
            print(e)

    elif response == "no":
        image_link = None
    else:
        image_link = None

    print(f'{Y}[+] {G}Searching profiles...')
    check_social_media(target_username, image_link)

if __name__ == "__main__":
    main()
