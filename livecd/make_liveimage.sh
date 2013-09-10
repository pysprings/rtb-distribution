VERSION='19.2'
RELEASEVER='19'
TITLE="PySprings RTB Live $VERSION"
PRODUCT="pysprings-rtb-$VERSION"

sudo livecd-creator --title="$TITLE" --product="$PRODUCT"  --releasever=$RELEASEVER -c pysprings-rtblive.ks
