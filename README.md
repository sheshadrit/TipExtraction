# A Tip Extractor for Yelp Reviews 
Prerequisite libraries required: `Pattern` and `SpaCy`

## Installation
Installing library pattern for python 3.0+:
1. Download pattern-master.zip from https://github.com/clips/pattern
2. Extract pattern-master.zip
3. Copy folder pattern to `%PATH%\Anaconda3\Lib\site-packages`

Installing library `SpaCy` for python 3.0+: 

Follow this link https://spacy.io/usage/

## Files List

<b>TipExtractor.py</b> : Uses spacy and pattern library to give summary of tip highlighted by uses most frequently

<b>TipExtractionWithoutSpacy.py</b> : Gives you a csv file contatining two columns review and extarcted tip

<b>ReviewsAndTips.csv</b>: A csv file contatining two columns review and extracted tip

<b>TipsAndTheirRank.csv</b>: Contains list of sentences from the extracted tip from `ReviewsAndTips.csv` file and there corresponding ranking i.e. how frequently they have used by the reviewers

<b>FinalExtractedTips.txt</b>: Contains list of sentences from the extracted tip from `ReviewsAndTips.csv` file which are most frequently used by reviewers

## Authors

[Sheshadri Talla](https://github.com/sheshadrit)

[Shrey Mudgal](https://github.com/samflynn)

## Copyright / License

Licensed under the GNU General Public License Version 2.0 (or later);
you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

   http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

