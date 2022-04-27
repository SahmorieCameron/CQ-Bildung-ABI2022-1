nextflow.enable.dsl = 2

params.hashlen = 51
params.outdir = "results"
params.indir = null


process velvet {
  publishDir "${params.outdir}", mode: "copy", overwrite: true
  container "https://depot.galaxyproject.org/singularity/velvet:1.2.10--hed695b0_3"
  input:
    path fastq
    val hashlen
  output:
    path "velvetdir"
  script:
    if(fastq instanceof List){
      """
      velveth velvetdir ${hashlen} -shortPaired -fastq -separate ${fastq}
      velvetg velvetdir
      """
    } else {
      """
      velveth velvetdir ${hashlen} -short -fastq ${fastq}
      velvetg velvetdir
      """
    }
}

workflow {
  fastqchannel = channel.fromPath("${params.indir}*.fastq").collect()
  fastqchannel.view()
  velvet(fastqchannel, params.hashlen)
}

//nextflow ../cq_pipelines2022/assembly.nf --indir results/fastp/
//velveth Assem 71 -short -fastq SRR16641643.fastq

// script:
//   if(fastq instanceof List){
//     """
//     velveth velvetdir ${hashlen} -shortPaired -fastq -separate ${fastq}
//     velveth velvetdir ${hashlen} -shortPaired -fastq -separate ${fastq[0]} ${fastq[1]}
//     """
//
//   } else {
//     """
//     velveth velvetdir ${hashlen} -fastq -short ${fastq}
//     velvetg velvetdir
//     """
//   }
// }
