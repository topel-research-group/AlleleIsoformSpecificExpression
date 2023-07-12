These samples have high quality throughout and contain no apparent adapters
* Trimmed with Cutadapt parameters `-m 40 -q 30,30`

ls *1.trimmed.fastq.gz | grep -o "ERR......." | while read i; do
	SAMPLE=${i}
	BR=$(grep -A13 "Command line" runCutadapt.sge.o32680 | grep -A13 $i | grep "Total reads processed" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	BB=$(grep -A13 "Command line" runCutadapt.sge.o32680 | grep -A13 $i | grep "Total basepairs processed" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	AR=$(grep -A13 "Command line" runCutadapt.sge.o32680 | grep -A13 $i | grep "Reads written" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	AB=$(grep -A13 "Command line" runCutadapt.sge.o32680 | grep -A13 $i | grep "Total written" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	echo -e "| ${SAMPLE} |  ${BR} | ${BB} |  ${AR} | ${AB} |" >> README.md
done


|   Sample   |          Before          |                  After                   |
|            |   Reads    |    Bases    |       Reads        |        Bases        |
|------------|------------|-------------|--------------------|---------------------|
| ERR3393443 | 14,333,570 | 731,012,070 | 14,075,228 (98.2%) | 714,446,148 (97.7%) |
| ERR3393444 | 13,040,361 | 665,058,411 | 12,799,309 (98.2%) | 649,755,204 (97.7%) |
| ERR3393445 | 12,981,433 | 662,053,083 | 12,769,967 (98.4%) | 648,379,181 (97.9%) |
| ERR3393446 | 10,381,800 | 529,471,800 | 10,208,658 (98.3%) | 518,256,884 (97.9%) |
| ERR3393447 | 14,789,928 | 754,286,328 | 14,539,639 (98.3%) | 738,142,599 (97.9%) |
| ERR3393448 | 12,462,075 | 635,565,825 | 12,232,886 (98.2%) | 620,996,594 (97.7%) |
| ERR3393449 | 12,483,932 | 636,680,532 | 12,254,542 (98.2%) | 622,128,494 (97.7%) |
| ERR3393450 | 11,656,306 | 594,471,606 | 11,456,129 (98.3%) | 581,686,679 (97.8%) |
| ERR3393451 |  9,334,521 | 476,060,571 |  9,166,232 (98.2%) | 465,378,593 (97.8%) |
| ERR3393452 | 13,949,392 | 711,418,992 | 13,706,618 (98.3%) | 695,895,431 (97.8%) |
| ERR3393453 | 10,513,202 | 536,173,302 | 10,325,756 (98.2%) | 524,260,243 (97.8%) |
| ERR3393454 | 13,745,864 | 701,039,064 | 13,504,348 (98.2%) | 685,635,353 (97.8%) |
| ERR3393455 | 10,681,304 | 544,746,504 | 10,495,243 (98.3%) | 532,797,372 (97.8%) |
| ERR3393456 | 13,016,448 | 663,838,848 | 12,812,758 (98.4%) | 650,563,294 (98.0%) |
