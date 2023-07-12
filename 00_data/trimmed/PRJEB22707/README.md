These samples have high quality throughout and contain no apparent adapters
* Trimming with Cutadapt parameters `-m 40 -q 30,30`

ls *1.trimmed.fastq.gz | grep -o "ERR......." | while read i; do
	SAMPLE=${i}
	BR=$(grep -A13 "Command line" runCutadapt.sge.o32681 | grep -A13 $i | grep "Total reads processed" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	BB=$(grep -A13 "Command line" runCutadapt.sge.o32681 | grep -A13 $i | grep "Total basepairs processed" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	AR=$(grep -A13 "Command line" runCutadapt.sge.o32681 | grep -A13 $i | grep "Reads written" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	AB=$(grep -A13 "Command line" runCutadapt.sge.o32681 | grep -A13 $i | grep "Total written" | cut -f2 -d':' | tr -d ' ' | tr -d '\n' | sed 's/bp/ bp/g' | sed 's/(/ (/g')
	echo -e "| ${SAMPLE} |  ${BR} | ${BB} |  ${AR} | ${AB} |" >> README.md
done


|   Sample   |          Before            |                  After                   |
|            |   Reads    |     Bases     |       Reads        |        Bases        |
|------------|------------|---------------|--------------------|---------------------|
| ERR2131466 | 18,472,821 |   942,113,871 | 17,564,057 (95.1%) | 884,528,304 (93.9%) |
| ERR2131467 | 16,077,353 |   819,945,003 | 15,295,426 (95.1%) | 770,327,351 (93.9%) |
| ERR2131468 | 19,991,027 | 1,019,542,377 | 18,996,930 (95.0%) | 956,387,280 (93.8%) |
| ERR2131469 | 20,490,581 | 1,045,019,631 | 19,490,130 (95.1%) | 981,493,424 (93.9%) |
| ERR2131470 | 19,656,403 | 1,002,476,553 | 18,690,295 (95.1%) | 941,292,735 (93.9%) |
| ERR2131471 | 19,092,972 |   973,741,572 | 18,167,027 (95.2%) | 914,842,927 (94.0%) |
| ERR2131472 | 19,297,374 |   984,166,074 | 18,352,149 (95.1%) | 924,166,524 (93.9%) |
| ERR2131473 | 18,257,082 |   931,111,182 | 17,371,735 (95.2%) | 874,886,681 (94.0%) |
| ERR2131474 | 17,103,021 |   872,254,071 | 16,269,667 (95.1%) | 819,346,395 (93.9%) |
| ERR2131475 | 14,793,149 |   754,450,599 | 14,078,791 (95.2%) | 709,069,724 (94.0%) |
| ERR2131476 | 16,831,949 |   858,429,399 | 16,003,033 (95.1%) | 805,813,934 (93.9%) |
| ERR2131477 | 15,526,700 |   791,861,700 | 14,761,177 (95.1%) | 743,410,960 (93.9%) |
