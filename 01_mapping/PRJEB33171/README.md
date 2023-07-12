#

For generating summary stats:

```
for i in ERR*; do
        QCED=$(grep "reads;" ${i}/runHisat2.sge.e* | cut -f1 -d' ')
        UNMAP=$(grep "aligned 0 times" ${i}/runHisat2.sge.e* | sed 's/^ *//g' | cut -f-2 -d' ')
        SINGMAP=$(grep "aligned exactly" ${i}/runHisat2.sge.e* | sed 's/^ *//g' | cut -f-2 -d' ')
        MULTIMAP=$(grep "aligned >1" ${i}/runHisat2.sge.e* | sed 's/^ *//g' | cut -f-2 -d' ')
        MAPPC=$(grep "overall" ${i}/runHisat2.sge.e* | cut -f1 -d' ')

        echo -e " ${QCED} | ${UNMAP} | ${SINGMAP} | ${MULTIMAP} |    ${MAPPC} |" >> README.md
done
```
