import requests


def fetch_all_papers(
    query, fields, sort="paperId:asc", publication_types=None, open_access_pdf=None
):
    base_url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"

    params = {
        "query": query,
        "fields": fields,
        "sort": sort,
    }

    if publication_types:
        params["publicationTypes"] = publication_types
    if open_access_pdf:
        params["openAccessPdf"] = open_access_pdf

    all_papers = []
    token = None

    while True:
        if token:
            params["token"] = token

        response = requests.get(base_url, params=params)
        response_data = response.json()

        if "data" in response_data:
            all_papers.extend(response_data["data"])
        else:
            break

        token = response_data.get("token")
        if not token:
            break

    return all_papers


if __name__ == "__main__":
    fields = (
        "paperId,corpusId,url,title,venue,publicationVenue,"
        "year,authors,externalIds,abstract,referenceCount,citationCount,"
        "influentialCitationCount,isOpenAccess,openAccessPdf,fieldsOfStudy,"
        "s2FieldsOfStudy,publicationTypes,publicationDate,journal,citationStyles"
    )
    data = fetch_all_papers(query='"research information system"', fields=fields)
