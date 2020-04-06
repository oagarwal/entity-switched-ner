This is the code for the paper 'Entity Switched Datasets'.<br/>

Currently it is limited to replacing all types of entities in CoNLL '03 data. We'll soon release the code for creating the rest of the datasets described in the paper as well.<br/>

Following are the steps to create the data - <br/>

<ol>
	<li>Follow the instructions <a href="https://www.clips.uantwerpen.be/conll2003/ner/">here</a> to obtain the CoNLL'03 data and generate eng.testb</li>
	<li>Run the script as follows - python3 switch_entities.py &lt;path-to-eng.testb&gt; &lt;path-to-entity-list&gt; &lt;path-to-ouput-file&gt;. Entity lists are under the entities folder.</li>
</ol>

