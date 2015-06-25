#include <vector>
#include <iostream>


using namespace std;

template<typename K, typename V>
struct MapPair {
  K key;
  V val;
  MapPair(K k, V v) : key(k), val(v) { }
};

template<typename K, typename V>
class SlowMap {
public:
  SlowMap() { }
  void insert(const K& k, const V& v);
  MapPair<K,V>* get(const K& k);

private:
  int find(const K& key) const;
  vector< MapPair<K,V> > storage_;

};

template <typename K, typename V>
void SlowMap<K,V>::insert(const K& k, const V& v)
{ 
  MapPair<K,V> p(k,v);
  int idx = find(k);
  if(idx == -1){
    storage_.push_back(p);
  }
  else {
    storage_[idx] = p;
  }
}

template <typename K, typename V>
MapPair<K,V>* SlowMap<K,V>::get(const K& k)
{
  int idx = find(k);
  if(idx != -1){
    return &storage_[idx];
  }
  return NULL;

}

template <typename K, typename V>
int SlowMap<K,V>::find(const K& key) const
{
  for(size_t i=0; i < storage_.size(); i++){
    if(key == storage_[i].key){
      return i;
    }
  }
  return -1;
}

int main()
{

  SlowMap<int,string> m1;
  MapPair<int, string>* ptr;
  string s = "Hi";
  m1.insert(5, s);
  s = "Bye";
  m1.insert(6, s);

  ptr = m1.get(5);
  if(ptr != NULL){
    cout << ptr->key << " " << ptr->val << endl;
  }
  else {
    cout << "5 does not exist in the map" << endl;
  }
    
  s = "Hello";
  m1.insert(5, s);
  ptr = m1.get(5);
  if(ptr != NULL){
    cout << ptr->key << " " << ptr->val << endl;
  }
  else {
    cout << "5 does not exist in the map" << endl;
  }


  return 0;
}
