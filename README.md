This is the code and data for the paper <a href="https://arxiv.org/abs/2004.04123">Entity-Switched Datasets: An Approach to Auditing the In-Domain Robustness of Named Entity Recognition Models</a>.<br/>

Currently it is limited to replacing all types of entities in CoNLL '03 data to produce the exact dataset used in the paper. We'll soon release the code for creating the rest of the datasets described in the paper as well. We'll also release the code to susbtitute any entities of your choice.<br/>

Following are the steps to create the data - <br/>

<ol>
	<li>Follow the instructions <a href="https://www.clips.uantwerpen.be/conll2003/ner/">here</a> to obtain the CoNLL'03 data and generate eng.testb</li>
	<li>Run the script as follows - python3 switch_entities.py &lt;path-to-eng.testb&gt; &lt;path-to-entity-list&gt; &lt;path-to-ouput-file&gt;. Entity lists are under the entities folder.</li>
</ol>

