# environmental-monitoring

The Finnish research stations from monitoring programmes analysis framework

## The task (initial)

The Finnish research stations have collected metadata from several long-term environmental monitoring programmes. 

The aim is that during the next 5 years all data from Kilpisjärvi, Lammi and Tvärminne stations 
will be opened according to FAIR principles?

Where would you start and what would be the most important steps / 
stages to achieve this goal?

## The task (formalized)

Task: To develop a strategy for the establishment of `Kilpisjärvi`, `Lammi` and `Tvärminne` stations 
over the next five years in accordance with FAIR principles

## FAIR principles 

FAIR data is a term outlining best practice for preserving research data. The FAIR principles that are used in this project are presented in Figure 1: 

<img src="https://www.ccdc.cam.ac.uk/media/FAIR-Image.png" width="750"/>

Figure 1. FAIR principles brief description (the picture was taken from [CCDC software website](https://www.ccdc.cam.ac.uk/solutions/about-the-csd/fair-data-principles/?utm_term=&utm_campaign=Performance+Max+-+CrossMiner&utm_source=adwords&utm_medium=ppc&hsa_acc=9348977139&hsa_cam=20546890251&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjw_qexBhCoARIsAFgBleuoks8GC0SdsuNmC5dOvXrvf2FJhPDD4mUh4W0vjf4q_vGhClp0ELAaAqQSEALw_wcB), 26.04.2024)

Thus, four FAIR principles are distinguished (below are short descriptions of each principle summarizing the key message): 

* **F**indability: For data to be findable there must be sufficient metadata and a unique and persistent identifier.
* **A**ccessibility: metadata and data should be readable by humans and by machines, and it must reside in a trusted repository
* **I**nteroperability: must share a common structure, and metadata must use recognized, formal terminologies for description
* **R**eusability: Data and collections must have clear usage licenses and clear provenance

## Proposal

This section presents the first version of the draft strategy that is proposed to be applied to the original data.

The aim: To develop a strategy for the establishment of `Kilpisjärvi`, `Lammi` and `Tvärminne` stations 
over the next five years in accordance with FAIR principles. 

In order to achieve the stated objective, the current document has been prepared and the following actions have been performed in the process of its preparation: 

- Evaluate the current structure of metadata and datasets. 
- Propose changes to the structure based on the evaluation. Criterion - "Interoperability"
- Propose a plan to improve the "Accessibility" criterion by creating dataset distribution services (API, versioning, etc.).
- Create a plan to improve the "Findability" criterion. For this purpose, it is proposed to use a robust identifier system
- Propose a plan to improve the "Reusability" criterion. 

Each of the items is described in more detail below. 

### Data exploration

Based on the results of a detailed comparison of the dataset columns of different stations, the following table was prepared:

Table 1. Observed issues per metadata dataset

|                      Column                      |  Issue per Kilpisjärvi dataset  |              Issue per  Lammi dataset              |  Issue per Tvärminne dataset  |
|:------------------------------------------------:|:-------------------------------:|:--------------------------------------------------:|:-----------------------------:|
|               Name of the dataset                |                ✓                |                         ✓                          |               ✓               |
|                     Station                      |                ✓                |                         ✓                          |         Presence nan          |
|           General description of data            |          Presence nan           |                    Presence nan                    |         Presence nan          |
|                     Location                     |          Presence nan           |                    Presence nan                    |     No data in the column     |
|                        X                         |      No data in the column      |                    Presence nan                    |     No data in the column     |
|                        Y                         |      No data in the column      |                    Presence nan                    |     No data in the column     |
|                Coordinate system                 |      No data in the column      |                    Presence nan                    |         Presence nan          |
|                 Environment type                 |                ✓                |                    Presence nan                    |         Presence nan          |
|                    Other type                    |      No data in the column      | Environment type column intersection, presence nan |     No data in the column     |
|                Measured variables                |  Duplicates due to long format  |           Duplicates due to long format            | Duplicates due to long format |
|                       Unit                       |     Presence nan and "???"      |                    Presence nan                    |         Presence nan          |
|                  Spatial extent                  |    Presence nan, not unified    |             Presence nan, not unified              |   Presence nan, not unified   |
|                Spatial resolution                |           Not unified           |                    Not unified                     |   Presence nan, not unified   |
|                 Temporal extent                  |    Presence nan, not unified    |             Presence nan, not unified              |   Presence nan, not unified   |
|                  Starting year                   |                ✓                |             Presence nan, not unified              |   Presence nan, not unified   |
|                     End year                     | Mixed types: integer and string |   Mixed types: integer and string, presence nan    |     No data in the column     |
|               Temporal resolution                |          Presence nan           |             Presence nan, not unified              |         Presence nan          |
|                    Data type                     |          Presence nan           |                    Presence nan                    |         Presence nan          |
|                      Format                      |          Presence nan           |                    Presence nan                    |         Presence nan          |
|          Is the dataset well described           |       Expected to be bool       |                Expected to be bool                 |         Presence nan          |
| In what databases the dataset has been described |          Presence nan           |                    Presence nan                    |         Presence nan          |
|    Is the dataset regurlarly shared somewhere    |          Presence nan           |                    Presence nan                    |         Presence nan          |
|        Is the data used in a publication         |          Presence nan           |                    Presence nan                    |   Presence nan, not unified   |
|                      Where                       |          Presence nan           |               No data in the column                |     No data in the column     |
|                      Owner                       |      Presence nan and "?"       |                    Presence nan                    |         Presence nan          |
|                   Other notes                    |                ✓                |                         ✓                          |               ✓               |
|                  Contact person                  |          Presence nan           |                    Presence nan                    |         Presence nan          |
|                   Institution                    |          Presence nan           |               No data in the column                |     No data in the column     |
|             KBS, omat muistiinpanot              |          Presence nan           |                     Not exist                      |               -               |
|                    LBA notes                     |                -                |                    Presence nan                    |               -               |

Thus, a set of actions is required to improve the metadata structure. 

### Step 1. Interoperability

Based on the results of the analysis of the table structure of the xlsx page of the file `Kilpisjärvi`, `Lammi`, `Tvärminne` it is proposed to perform the following actions, which will make the metadata structure more simple, understandable and comparable:

- `Station` column: It is required to enter station identifiers into the table (for station Tvärminne) and prepare a separate document listing all possible identifiers for each station abbreviation
- `General description of data` column: Need to fill in the gaps for stations Kilpisjärvi, Lammi and Tvärminne
- `Location` column: Need to fill in the gaps for stations Kilpisjärvi, Lammi and Tvärminne
- `X`, `Y` and `Coordinate system`: it is proposed to indicate WGS84 coordinates everywhere instead of local metric systems (this will allow users to find a point more easily in both Google maps and other ones, as well as such coordinates are much easier to understand than multi-cypher coordinates from metric systems).
- `Environment type`, `Other type`: предлагается обьединить эти колонки и сделать

General suggestions for improving interoperability:
- Allow datasets to be uploaded in multiple formats, or allow the user to interact with the data through a REST API. Possible examples: Parquet, CSV, Excel, JSON, GEOJSON, Geopackage, shapefile. Converters of tabular data to such formats can be reused in other data catalogs.

### Step 2. Accessibility

To make data accessible in the modern digital world, it is proposed to build a datahub ecosystem where data can be accessed using two modes: 

- Manual downloading of datasets in desired format;
- Data request via REST API

Realization of both ways of interaction requires implementation and deployment of the backend service. An example of 
such a service implemented using the technology stack `Python, Docker, heroku platform`: [API environmental monitoring service]()

Service versioning should be prepared for researchers and engineers. For example, when providing 
API access to a data platform, both semantic versioning of datasets, as well as the API of the service. 
Then, when changing the data structure, using old references and methods, researchers will be able to get the same datasets.

Examples of data platforms with relatively small budgets (can be used as references): 
- [http://dataportal.saeri.org/](http://dataportal.saeri.org/) - Falklands islands data catalog

### Step 3. Findability

Persistent identifiers are required for Findability. 
Ensuring the availability of such identifiers is proposed through the use of DOIs. 
This will also allow such data to be easily used and cited in scientific publications. 

Example of data platforms that uses DOI generation: 
- [https://techdocs.gbif.org/en/](https://techdocs.gbif.org/en/) - Global Biodiversity Information Facility (GBIF)
- [https://doi.org/10.15468/dl.f487j5](https://doi.org/10.15468/dl.f487j5) - GBIF.org (20 October 2023) GBIF Occurrence Download

### Step 4. Reusability

The final processing activities should be the preparation of license documents and verification that the data have a clear provenance.
To ensure Reusability, it is also necessary to describe in detail the structure of the datasets provided. This can be done by means of 
a single web page (as a simplified example) - see [environmental-monitoring test assignment description]()

## Used literature 

1) [Open and FAIR data sharing policy related to writing](https://authorservices.taylorandfrancis.com/data-sharing-policies/open-and-fair/)
2) [CCDC FAIR data principles](https://www.ccdc.cam.ac.uk/solutions/about-the-csd/fair-data-principles/?utm_term=&utm_campaign=Performance+Max+-+CrossMiner&utm_source=adwords&utm_medium=ppc&hsa_acc=9348977139&hsa_cam=20546890251&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjw_qexBhCoARIsAFgBleuoks8GC0SdsuNmC5dOvXrvf2FJhPDD4mUh4W0vjf4q_vGhClp0ELAaAqQSEALw_wcB)
3) [Common Data Elements: Standardizing Data Collection. Data Definition of FAIR Data](https://www.nlm.nih.gov/oet/ed/cde/tutorial/02-200.html)