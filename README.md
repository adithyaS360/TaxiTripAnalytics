# Taxi Trip Analytics

A local Apache Spark application for analyzing NYC yellow taxi trips from January 2025. It produces summary CSVs, trip clusters, and fare-model results.

## Requirements

- JDK 17
- Maven 3.9 or newer
- Python 3.9 or newer only if generating charts

Spark 3.5.3 is configured in `pom.xml`. The required JVM module options are in `.mvn/jvm.config`.

## Run the analysis

From this directory, run:

```powershell
mvn clean compile exec:java
```

Make sure Maven is using JDK 17. The first run downloads Spark and its dependencies and may take several minutes. The input files are included under `data/`.

The program writes CSV results to `out/`.

## Generate charts (optional)

After the Java analysis completes:

```powershell
python -m pip install -r requirements.txt
python charts_real.py
```

Chart images are written to `out/` as well.
