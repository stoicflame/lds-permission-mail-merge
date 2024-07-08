# LDS Permission Mail Merge

Have all the parents fill out a duplicate of this form:

https://forms.gle/xpV4YZePPkKcBPt4A

Export the results to CSV file `/tmp/camp-responses.csv`.

Download the permission form from here:

https://assets.churchofjesuschrist.org/ec/6a/ec6a32b2ded011eda8abeeeeac1eefc32321140e/2017_parental_or_guardian_permission_medical_release.pdf

and save it to `/tmp/2017_parental_or_guardian_permission_medical_release.pdf`.

Edit `field-template.xml` to include the details of your specific event.

Run:

```
python csv-to-fdf.py
mkdir /tmp/camp-permissions
bash fdf-to-pdf.sh
```


