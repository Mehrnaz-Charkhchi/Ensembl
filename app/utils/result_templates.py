def gene_result_template(gene_model: list) -> dict:
    gene_results_dict = {"results": []}
    for gene_result in gene_model:
        gene_dict = {"gene name": gene_result.stable_id,
                     "location": gene_result.location,
                     "Ensembl stable ID ": gene_result.display_label,
                     "species": gene_result.species}
        gene_results_dict["results"].append(gene_dict)

    return gene_results_dict
