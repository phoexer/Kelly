# Convert CSV

This script convert my Stanchart statement to YNAB compartible CSV so I can upload.
This was a quick and dirty hack that did what I needed it to do, it's not very ellegant and has a lot of features missing.

I'll probably get back to it later... but then again I probably won't

## TODO
- Use ML Classification to try guess the category, I have enough data for that now I think
- Change output to OFX and QFX, hmmm, that would mean I would need to change the name of the script too right?
- ...
- Profits!

## Notes
### Classification
I got started on the classification problem. Making that data ML ready was quite interesting, I ended up wasting the whole 
afternoon just trying to tune it so that it predicts a bit more accurately. 
Thus far I'm using a number of classification models, and the accuracy is up to around 0.826815642458 ± 0.03

## TO DONE
- Allow the usage of runtime parameters and stop hard coding the filenames