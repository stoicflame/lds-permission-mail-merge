# LDS Permission Mail Merge

Have all the parents fill out a duplicate of this form:

https://forms.gle/xpV4YZePPkKcBPt4A

Export the results to CSV file `/tmp/camp-responses.csv`.

Run:

```
python csv-to-fdf.py
mkdir /tmp/camp-permissions
bash fdf-to-pdf.sh
```


