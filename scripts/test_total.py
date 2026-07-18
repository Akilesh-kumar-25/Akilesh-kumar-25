import urllib.request, re

html = urllib.request.urlopen('https://github.com/Akilesh-kumar-25').read().decode('utf-8')
matches = re.findall(r'id="year-link-(\d{4})"', html)
print("Years:", matches)

total = 0
for year in matches:
    url = f"https://github.com/users/Akilesh-kumar-25/contributions?from={year}-01-01&to={year}-12-31"
    year_html = urllib.request.urlopen(url).read().decode('utf-8')
    m = re.search(r'(\d{1,3}(?:,\d{3})*)\s+contributions\s+in\s+' + year, year_html)
    if m:
        count = int(m.group(1).replace(',', ''))
        print(f"Year {year}: {count}")
        total += count

print("Total:", total)
